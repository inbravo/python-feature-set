# Created on 2023-10-05 11:00
# Script to extract file information from a directory and save it to an Excel file
# -*- inbravo@github -*-
import os
from datetime import datetime

import pandas as pd


def get_file_info(root_dir):
    """
    Retrieve metadata information for all files in a given directory.
    This function traverses the directory tree starting from the specified root directory
    and collects metadata for each file, including its name, path, size, creation time,
    and last modification time.
    Args:
        root_dir (str): The root directory to start traversing for files.
    Returns:
        list[dict]: A list of dictionaries, where each dictionary contains metadata
        about a file with the following keys:
            - "Folder Name" (str): The name of the folder containing the file.
            - "File Name" (str): The name of the file.
            - "File Path" (str): The full path to the file.
            - "Size (KB)" (float): The size of the file in kilobytes, rounded to 2 decimal places.
            - "Created" (str): The creation timestamp of the file in the format "YYYY-MM-DD HH:MM:SS".
            - "Last Modified" (str): The last modification timestamp of the file in the format "YYYY-MM-DD HH:MM:SS".
    Raises:
        Exception: If an error occurs while reading a file's metadata, it will be caught
        and logged, but the function will continue processing other files.
    """
    file_data = []

    for foldername, _, filenames in os.walk(root_dir):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            try:
                stats = os.stat(file_path)
                file_info = {
                    "Folder Name": os.path.basename(foldername),
                    "File Name": filename,
                    "File Path": file_path,
                    "Size (KB)": round(stats.st_size / 1024, 2),
                    "Created": datetime.fromtimestamp(stats.st_ctime).strftime(
                        "%Y-%m-%d %H:%M:%S"
                    ),
                    "Last Modified": datetime.fromtimestamp(stats.st_mtime).strftime(
                        "%Y-%m-%d %H:%M:%S"
                    ),
                }
                file_data.append(file_info)
            except Exception as e:
                print(f"Error reading {file_path}: {e}")

    return file_data


def save_to_excel(file_data, output_file="file_report.xlsx"):
    df = pd.DataFrame(file_data)
    df.to_excel(output_file, index=False)
    print(f"File report saved to {output_file}")


directory_to_scan = (
    "//Users/inbravo//Library//CloudStorage//OneDrive-Impetus//leaplogic-sales-presales-repo//"
)

# Ensure the directory exists
if not os.path.exists(directory_to_scan):
    raise ValueError(f"The directory {directory_to_scan} does not exist.")
file_info_list = get_file_info(directory_to_scan)
save_to_excel(file_info_list)
