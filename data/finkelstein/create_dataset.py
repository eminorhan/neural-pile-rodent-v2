import os
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


def extract_subject_session_id(file_path):
    """
    Extracts subject and session identifier strings from a full file path.

    Args:
        file_path (str): The full file path.

    Returns:
        str: SUbject identifier string.
        str: Session identifier string.
    """
    directory, filename = os.path.split(file_path)
    subdirectory = os.path.basename(directory)
    filename_without_extension, _ = os.path.splitext(filename)
    return f"{subdirectory}", f"{filename_without_extension}"


def get_args_parser():
    parser = argparse.ArgumentParser('Consolidate data in multiple files into a single file', add_help=False)
    parser.add_argument('--data_dir',default="data",type=str, help='Data directory')
    parser.add_argument('--hf_repo_name',default="eminorhan/finkelstein",type=str, help='processed dataset will be pushed to this HF dataset repo')
    parser.add_argument('--token_count_limit',default=10_000_000, type=int, help='sessions with larger token counts than this will be split into chunks (default: 10_000_000)')
    parser.add_argument('--bin_size',default=0.02, type=float, help='time bin size (in seconds) for calculating spike counts (default: 0.02)')
    return parser


if __name__ == '__main__':

    args = get_args_parser()
    args = args.parse_args()
    print(args)

    # get all .nwb files in the sorted folder
    nwb_files = find_nwb_files(args.data_dir)
    print(f"Files: {nwb_files}")
    print(f"Total number of files: {len(nwb_files)}")

    # lists to store results for each session
    spike_counts_list, subject_list, session_list, segment_list = [], [], [], []

    # token counter
    n_tokens = 0

    for file_path in sorted(nwb_files):
        print(f"Processing file: {file_path}")
        with NWBHDF5IO(file_path, "r") as io:
            nwbfile = io.read()

            # we will save just spike activity
            units = nwbfile.units.to_dataframe()
            max_time = max([u.max() for u in units['spike_times']])
            spike_counts = np.vstack([np.histogram(row, bins=np.arange(0, max_time + args.bin_size, args.bin_size))[0] for row in units['spike_times']]).astype(np.uint8)  # spike count matrix (nxt: n is #channels, t is time bins)

            # subject, session identifiers
            subject_id, session_id = extract_subject_session_id(file_path)

            # token count of current session
            total_elements = np.prod(spike_counts.shape)

            # append sessions
            # if session data is large, divide spike_counts array into smaller chunks
            if total_elements > args.token_count_limit:
                n_channels, n_time_bins = spike_counts.shape
                num_segments = math.ceil(total_elements / args.token_count_limit)
                segment_size = math.ceil(n_time_bins / num_segments)
                print(f"Spike count shape / max: {spike_counts.shape} / {spike_counts.max()}. Dividing into {num_segments} smaller chunks ...")
                for i in range(num_segments):
                    start_index = i * segment_size
                    end_index = min((i + 1) * segment_size, n_time_bins)
                    sub_array = spike_counts[:, start_index:end_index]
                    spike_counts_list.append(sub_array)
                    subject_list.append(subject_id)
                    session_list.append(session_id)
                    segment_list.append(f"segment_{i}")
                    print(f"Divided into segment_{i} with shape / max: {sub_array.shape} / {sub_array.max()}")
                    n_tokens += np.prod(sub_array.shape)
            else:
                spike_counts_list.append(spike_counts)
                subject_list.append(subject_id)
                session_list.append(session_id)
                segment_list.append("segment_0")  # default segment id
                print(f"Spike count shape / max: {spike_counts.shape} / {spike_counts.max()} (segment_0)")
                n_tokens += np.prod(spike_counts.shape)

    def gen_data():
        for a, b, c, d in zip(spike_counts_list, subject_list, session_list, segment_list):
            yield {
                "spike_counts": a,
                "subject_id": b,
                "session_id": c,
                "segment_id": d
                }
            
    ds = Dataset.from_generator(gen_data, writer_batch_size=1)
    print(f"Number of tokens in dataset: {n_tokens} tokens")
    print(f"Number of rows in dataset: {len(ds)}")

    # push all data to hub 
    ds.push_to_hub(args.hf_repo_name, max_shard_size="1GB", token=True)