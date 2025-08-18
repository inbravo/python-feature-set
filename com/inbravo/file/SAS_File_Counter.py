import os
import sys
import logging
from typing import Union

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def count_sas_files(directory: str) -> int:
    """
    Counts the number of '.sas' files in the given directory and its subdirectories.

    Args:
        directory (str): The path to the directory to search.

    Returns:
        int: The count of '.sas' files.
    """
    sas_file_count = 0
    for root, _, files in os.walk(directory):
        sas_file_count += sum(1 for file in files if file.endswith(".sas"))
    return sas_file_count


def validate_directory(directory: str) -> Union[str, None]:
    """
    Validates if the given directory exists and is a directory.

    Args:
        directory (str): The path to validate.

    Returns:
        str: The validated directory path if valid.
        None: If the directory is invalid.
    """
    if not os.path.exists(directory):
        logging.error("The provided path does not exist.")
        return None
    if not os.path.isdir(directory):
        logging.error("The provided path is not a directory.")
        return None
    return directory


if __name__ == "__main__":
    # Check if a folder path is provided as a command-line argument
    if len(sys.argv) < 2:
        print("Usage: python file_count.py <folder_path>")
        sys.exit(1)

    folder_path = sys.argv[1]

    # Validate the folder path
    valid_directory = validate_directory(folder_path)
    if not valid_directory:
        print("Invalid folder path. Please provide a valid directory.")
        sys.exit(1)

    try:
        count = count_sas_files(valid_directory)
        if count == 0:
            print("No '.sas' files found in the specified directory.")
        else:
            print(f"Number of '.sas' files: {count}")
    except PermissionError:
        logging.error("Permission denied. Please check your folder permissions.")
        print("Permission denied. Please check your folder permissions.")
    except FileNotFoundError as e:
        logging.error("File not found: %s", e)
        print(f"File not found: {e}")
    except OSError as e:
        logging.error("OS error occurred: %s", e)
        print(f"OS error occurred: {e}")