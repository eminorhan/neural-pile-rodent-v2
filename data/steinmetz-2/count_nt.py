import os
import math
import argparse
import numpy as np
from scipy.io import loadmat
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
            if filename.endswith(".mat"):
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


def create_spike_count_matrix(x, bin_size=0.02):
    """
    Processes a list of lists containing spike times and cluster indices, 
    differentiating clusters across probes, to create a spike count matrix.

    Args:
        x: A list of 8 sublists, where each sublist contains spike times and cluster indices.
           x[probe_idx][0] -> spike times (t, 1) numpy array
           x[probe_idx][1] -> cluster indices (t, 1) numpy array
        bin_size: The size of each time bin in seconds (default: 0.02 seconds).

    Returns:
        A numpy array of shape (n_clusters, n_timebins) representing spike counts per cluster and time bin.
    """

    all_spike_times = []
    all_cluster_indices = []
    
    # offset the cluster indices so that they are unique across probes.
    cluster_offset = 0
    for probe_idx, probe in enumerate(x):
        
        print(f"(Probe {probe_idx}) Spike times     min/max/dtype: {probe[0].min()}, {probe[0].max()}, {probe[0].dtype}")
        print(f"(Probe {probe_idx}) Cluster indices min/max/dtype: {probe[1].min()}, {probe[1].max()}, {probe[1].dtype}")

        spike_times, cluster_indices = probe[0], probe[1].astype(np.uint16)
        all_spike_times.extend(spike_times.flatten().tolist())
        all_cluster_indices.extend((cluster_indices.flatten() + cluster_offset).tolist())
        cluster_offset += np.max(cluster_indices) # set the offset to be larger than the max cluster index in the current probe.

    all_spike_times = np.array(all_spike_times)
    all_cluster_indices = np.array(all_cluster_indices)

    # find the maximum time across all probes to determine the number of time bins
    min_time = np.min(all_spike_times)
    max_time = np.max(all_spike_times)
    n_timebins = int(np.ceil((max_time - min_time) / bin_size))

    # find the maximum cluster index to determine the number of clusters
    max_cluster = int(np.max(all_cluster_indices))
    n_clusters = max_cluster

    # initialize the spike time matrix with zeros
    spike_time_matrix = np.zeros((n_clusters, n_timebins), dtype=np.uint8)

    # populate the spike time matrix
    for spike_time, cluster_index in zip(all_spike_times, all_cluster_indices):
        time_bin = int((spike_time - min_time) / bin_size)
        spike_time_matrix[int(cluster_index)-1, time_bin] += 1

    return spike_time_matrix


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

        data = loadmat(file_path)['spks'][0]
        spike_counts = create_spike_count_matrix(data, bin_size=args.bin_size)

        neurons.append(spike_counts.shape[0])
        times.append(spike_counts.shape[1])
            
    print(f"({len(neurons)}) Neurons: {neurons}")
    print(f"({len(times)}) Times: {times}")