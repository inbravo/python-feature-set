import os
import time
import shutil
import argparse
from datetime import datetime


# define file categories and their extensions using DICTIONARY
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi", ".flv", ".wmv"],
    "Audios": [".mp3", ".wav", ".aac", ".flac", ".ogg"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
    "Scripts": [".py", ".js", ".sh", ".bat", ".java", ".cpp", ".c"],
}

def main() -> None:
    """Parse command-line arguments and execute the file organizer."""
    parser = argparse.ArgumentParser(
        description="Organize files in a directory into categorized subfolders."
    )
    parser.add_argument("--path", required=True, help="Directory path to organize.")
    parser.add_argument(
        "--interval",
        type=int,
        default=0,
        help="Interval (in minutes) to repeat automatically (0 = run once).",
    )
    args = parser.parse_args()

    if not os.path.exists(args.path):
        print(f"Path not found: {args.path}")
        return

    print(f"Watching directory: {args.path}")
    print("Organizer started. Press Ctrl+C to stop.\n")

    try:
        while True:
            organize_files(args.path)
            if args.interval == 0:
                break
            print(f"Waiting {args.interval} minutes before next run...\n")
            time.sleep(args.interval * 60)
    except KeyboardInterrupt:
        print("\nOrganizer stopped by user.")


if __name__ == "__main__":
    main()
    
# Function to organize files
def organize_files(base_path: str) -> None:
    """
    Organize files in the given directory into subfolders by category.

    Args:
        base_path: Path of the directory to organize.
    """
    # get list of files (not folders) in the base_path
    files = [
        f for f in os.listdir(base_path) if os.path.isfile(os.path.join(base_path, f))
    ]
    # If files list is empty
    if not files:
        print(f"[{datetime.now().strftime('%H:%M:%S')}] No files found in {base_path}")
        return

    # iterate through each file and move to respective category folder
    for file_name in files:
        source = os.path.join(base_path, file_name)
        print("source:", source)

        file_ext = os.path.splitext(file_name)[1]
        category = get_file_category(file_ext)
        target_folder = os.path.join(base_path, category)
        create_folder(target_folder)

        try:
            shutil.move(source, os.path.join(target_folder, file_name))
            print(
                f"[{datetime.now().strftime('%H:%M:%S')}] Moved: {file_name} -> {category}/"
            )
        except Exception as e:
            print(
                f"[{datetime.now().strftime('%H:%M:%S')}] Error moving {file_name}: {e}"
            )

# get file category based on extension
def get_file_category (file_extension: str) -> str:
    """Get file category based on extension."""
    for category, extensions in FILE_CATEGORIES.items():
        if file_extension.lower() in extensions:
            return category
    return "Others"

# create folder based on user provided name
def create_folder (folder_path: str) -> None:
    """Create folder if do not exist."""
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)    