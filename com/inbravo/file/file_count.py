import os
import sys

def count_sas_files(directory):
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


if __name__ == "__main__":
    # Check if a folder path is provided as a command-line argument
    if len(sys.argv) < 2:
        print("Usage: python file_count.py <folder_path>")
        sys.exit(1)

    folder_path = sys.argv[1]

    # Validate the folder path
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        try:
            count = count_sas_files(folder_path)
            print(f"Number of '.sas' files: {count}")
        except PermissionError:
            print("Permission denied. Please check your folder permissions.")
        except Exception as e:
            print(f"An error occurred: {e}")
    else:
        print("Invalid folder path.")
        print("Please provide a valid directory path.")
        print("Example: /path/to/your/folder")