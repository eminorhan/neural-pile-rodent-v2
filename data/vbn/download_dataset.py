import pandas as pd
import requests
import os
import argparse

def download_nwb_files(csv_file, output_dir):
    """
    Download NWB files based on ecephys_session_ids from a CSV file.

    Args:
        csv_file (str): Path to the CSV file containing ecephys_session_ids.
        output_dir (str): Directory to save the downloaded NWB files.
    """

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    try:
        df = pd.read_csv(csv_file)
        session_ids = df['ecephys_session_id'].tolist()
        total_files = len(session_ids)
        downloaded_count = 0

        for session_id in session_ids:
            url = f"https://visual-behavior-neuropixels-data.s3.us-west-2.amazonaws.com/visual-behavior-neuropixels/behavior_ecephys_sessions/{session_id}/ecephys_session_{session_id}.nwb"
            filename = os.path.join(output_dir, f"ecephys_session_{session_id}.nwb")

            try:
                response = requests.get(url, stream=True)
                response.raise_for_status()  # raise HTTPError for bad responses (4xx or 5xx)

                with open(filename, 'wb') as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        if chunk:
                            f.write(chunk)

                downloaded_count += 1
                print(f"Downloaded: {filename} ({downloaded_count} of {total_files} files)")

            except requests.exceptions.RequestException as e:
                print(f"Error downloading {url}: {e}")
            except Exception as e:
                print(f"An unexpected error occurred while downloading {url}: {e}")

    except FileNotFoundError:
        print(f"Error: CSV file '{csv_file}' not found.")
    except KeyError:
        print("Error: 'ecephys_session_id' column not found in the CSV file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download NWB files from a CSV.")
    parser.add_argument("csv_file", help="Path to the CSV file containing ecephys_session_ids.")
    parser.add_argument("--output_dir", default="data", help="Directory to save the downloaded NWB files (default: nwb_files).")

    args = parser.parse_args()

    download_nwb_files(args.csv_file, args.output_dir)