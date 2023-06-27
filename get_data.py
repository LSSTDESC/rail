"""Utility script to check for existence of data and curl missing files"""

import os
import argparse


def check_and_curl_data():
    """ 
    Check whether each data file exists at its specified local_path. If no such 
    file is found, curl a new copy from the specified remote_path. 

    Use -v flag to monitor each file that is handled.
    """

    data_files = [
        {
            "local_path": "src/rail/examples_data/goldenspike_data/data/base_catalog.pq",
            "remote_path": "https://portal.nersc.gov/cfs/lsst/PZ/base_catalog.pq"
        }
    ]

    # For handling verbose flag
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", action="store_true")
    args = parser.parse_args()

    for data_file in data_files:
        if args.verbose:
            print(f'Check file: {data_file["local_path"]}')
        if not os.path.exists(data_file["local_path"]):
            os.system(f'curl -o {data_file["local_path"]} {data_file["remote_path"]} --create-dirs')


if __name__ == "__main__":
    check_and_curl_data()
