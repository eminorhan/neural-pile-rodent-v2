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
        str: Subject identifier string.
        str: Session identifier string.
    """
    directory, filename = os.path.split(file_path)
    subdirectory = os.path.basename(directory)
    filename_without_extension, _ = os.path.splitext(filename)
    return f"{subdirectory}", f"{filename_without_extension}"


def get_args_parser():
    parser = argparse.ArgumentParser('Consolidate data in multiple files into a single file', add_help=False)
    parser.add_argument('--data_dir',default="data",type=str, help='Data directory')
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

    neurons = []
    times = []

    for file_path in sorted(nwb_files):
        print(f"Processing file: {file_path}")
        with NWBHDF5IO(file_path, "r") as io:
            nwbfile = io.read()

            # we will save just spike activity
            units = nwbfile.units.to_dataframe()
            max_time = max([u.max() if len(u)>0 else 0 for u in units['spike_times']])
            spike_counts = np.vstack([np.histogram(row, bins=np.arange(0, max_time + args.bin_size, args.bin_size))[0] for row in units['spike_times']]).astype(np.uint8)  # spike count matrix (nxt: n is #channels, t is time bins)

            neurons.append(spike_counts.shape[0])
            times.append(spike_counts.shape[1])
            
    print(f"({len(neurons)}) Neurons: {neurons}")
    print(f"({len(times)}) Times: {times}")