import os
import re
import math
import argparse
import numpy as np
from pynwb import NWBHDF5IO
from datasets import Dataset


def find_nwb_files(root_dir):
    """
    Crawls through a directory (including subdirectories), finds all files
    that end with ".nwb", and returns the full paths of all the found files in a list.

    Args:
        root_dir: The root directory to start the search from.

    Returns:
        A list of full paths to the found .nwb files, or an empty list if
        no files are found or if the root directory is invalid.
        Returns None if root_dir is not a valid directory.
    """

    if not os.path.isdir(root_dir):
        print(f"Error: '{root_dir}' is not a valid directory.")
        return None

    nwb_files = []
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith(".nwb"):
                full_path = os.path.join(dirpath, filename)
                nwb_files.append(full_path)
    return nwb_files


def get_args_parser():
    parser = argparse.ArgumentParser('Consolidate data in multiple files into a single file', add_help=False)
    parser.add_argument('--data_dir',default="data",type=str, help='Data directory')
    parser.add_argument('--hf_repo_name',default="eminorhan/lemerre",type=str, help='processed dataset will be pushed to this HF dataset repo')
    parser.add_argument('--token_count_limit',default=10_000_000, type=int, help='sessions with larger token counts than this will be split into chunks (default: 10_000_000)')
    parser.add_argument('--bin_size',default=0.02, type=float, help='time bin size (in seconds) for calculating spike counts (default: 0.02)')
    return parser


if __name__ == '__main__':

    args = get_args_parser()
    args = args.parse_args()
    print(args)

    # get all .nwb files in the sorted folder
    nwb_files = find_nwb_files(args.data_dir)
    if not nwb_files:
        print("No .nwb files found. Exiting.")
        exit()
    
    print(f"Total number of files found: {len(nwb_files)}")

    # --- New Grouping Logic ---
    session_groups = {}
    print("Grouping files by session...")
    for file_path in sorted(nwb_files):
        directory, filename = os.path.split(file_path)
        filename_without_extension, _ = os.path.splitext(filename)
        
        # Extract subject from directory
        subject_id = os.path.basename(directory)
        
        # Extract session part from filename
        # e.g., 'sub-PL081_ses-PL081-20230620-probe0_behavior+ecephys'
        base_name = filename_without_extension
        # Remove subject prefix from filename if it exists
        if base_name.startswith(subject_id + "_"):
            base_name = base_name[len(subject_id) + 1:] # e.g., 'ses-PL081-20230620-probe0_behavior+ecephys'
        
        # Get part before modality
        session_part = base_name.split('_')[0] # e.g., 'ses-PL081-20230620-probe0'
        
        # Create group key by removing probe info (e.g., '-probe0', '_probe1')
        session_group_id = re.sub(r'([-_])probe\d+$', '', session_part) # e.g., 'ses-PL081-20230620'
        
        # The unique key for a session is the combination of subject and session group
        unique_group_key = (subject_id, session_group_id)

        if unique_group_key not in session_groups:
            session_groups[unique_group_key] = []
        session_groups[unique_group_key].append(file_path)
    
    print(f"Found {len(session_groups)} unique session groups.")
    # --- End New Grouping Logic ---


    # lists to store results for each session
    spike_counts_list, subject_list, session_list, segment_list = [], [], [], []

    # token counter
    n_tokens = 0

    # --- Updated Main Loop: Iterate over session groups ---
    for (subject_id, session_id), file_paths in session_groups.items():
        print(f"\nProcessing session group: Subject={subject_id}, Session={session_id} ({len(file_paths)} file(s))")
        
        probe_data_to_bin = []
        session_max_time = 0

        # --- Pass 1: Read all files in the group to get max time and units ---
        for file_path in file_paths:
            print(f"  Reading file: {file_path}")
            try:
                with NWBHDF5IO(file_path, "r") as io:
                    nwbfile = io.read()
                    units = nwbfile.units.to_dataframe()
                    
                    file_max_time = 0
                    if not units.empty:
                        # Find max time for this file, handling empty spike trains
                        file_max_time = max([u.max() for u in units['spike_times'] if len(u) > 0], default=0)
                    
                    session_max_time = max(session_max_time, file_max_time)
                    probe_data_to_bin.append(units)
            except Exception as e:
                print(f"    ERROR reading file {file_path}: {e}. Skipping this file.")

        if session_max_time == 0 or not probe_data_to_bin:
            print("  Skipping session: no valid spike data found.")
            continue

        # --- Pass 2: Define shared bins and create concatenated array ---
        # Define shared time bins for the *entire* session group
        time_bins = np.arange(0, session_max_time + args.bin_size, args.bin_size)
        
        concatenated_spike_counts_parts = []
        
        for units in probe_data_to_bin:
            if units.empty:
                # Add an empty array with the correct time dimension
                concatenated_spike_counts_parts.append(np.empty((0, len(time_bins) - 1), dtype=np.uint8))
            else:
                # Bin spike times using the shared time_bins
                # This automatically handles padding: shorter recordings will have 0s at the end
                spike_counts = np.vstack([np.histogram(row, bins=time_bins)[0] for row in units['spike_times']]).astype(np.uint8)
                concatenated_spike_counts_parts.append(spike_counts)

        # Concatenate all probe arrays along the neuron axis (axis=0)
        combined_spike_counts = np.concatenate(concatenated_spike_counts_parts, axis=0)
        
        if combined_spike_counts.shape[0] == 0:
            print("  Skipping session: combined array has 0 neurons.")
            continue

        # --- Original Chunking Logic (now applied to the combined array) ---
        total_elements = np.prod(combined_spike_counts.shape)

        # if session data is large, divide combined_spike_counts array into smaller chunks
        if total_elements > args.token_count_limit:
            n_channels, n_time_bins = combined_spike_counts.shape
            num_segments = math.ceil(total_elements / args.token_count_limit)
            segment_size = math.ceil(n_time_bins / num_segments)
            print(f"Combined spike count shape / max: {combined_spike_counts.shape} / {combined_spike_counts.max()}. Dividing into {num_segments} smaller chunks ...")
            for i in range(num_segments):
                start_index = i * segment_size
                end_index = min((i + 1) * segment_size, n_time_bins)
                sub_array = combined_spike_counts[:, start_index:end_index]
                spike_counts_list.append(sub_array)
                subject_list.append(subject_id)
                session_list.append(session_id)
                segment_list.append(f"segment_{i}")
                print(f"  Divided into segment_{i} with shape / max: {sub_array.shape} / {sub_array.max()}")
                n_tokens += np.prod(sub_array.shape)
        else:
            spike_counts_list.append(combined_spike_counts)
            subject_list.append(subject_id)
            session_list.append(session_id)
            segment_list.append("segment_0")  # default segment id
            print(f"Combined spike count shape / max: {combined_spike_counts.shape} / {combined_spike_counts.max()} (segment_0)")
            n_tokens += np.prod(combined_spike_counts.shape)

    # --- Original Dataset Creation and Upload Logic (unchanged) ---
    def gen_data():
        for a, b, c, d in zip(spike_counts_list, subject_list, session_list, segment_list):
            yield {
                "spike_counts": a,
                "subject_id": b,
                "session_id": c,
                "segment_id": d
                }
            
    ds = Dataset.from_generator(gen_data, writer_batch_size=1)
    print(f"\nTotal number of tokens in dataset: {n_tokens} tokens")
    print(f"Total number of rows in dataset: {len(ds)}")

    # push all data to hub 
    print(f"Pushing dataset to hub: {args.hf_repo_name}")
    ds.push_to_hub(args.hf_repo_name, max_shard_size="1GB", token=True)
    print("Done.")