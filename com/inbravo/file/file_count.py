import os

def count_sas_files(directory):
    sas_file_count = 0
    for root, _, files in os.walk(directory):
        sas_file_count += sum(1 for file in files if file.endswith(".sas"))
    return sas_file_count


if __name__ == "__main__":
    folder_path = "//Users//inbravo//Library//CloudStorage//OneDrive-Impetus//pam//customer_artifacts//[2025]-[bfsi]-[ageas]-[leaplogic]-[sas-oracle-to-fabric-migration]//from_customer//code-recieved/Ageas"
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        count = count_sas_files(folder_path)
        print(f"Number of '.sas' files: {count}")
    else:
        print("Invalid folder path.")
        print("Please provide a valid directory path.")
        print("Example: /path/to/your/folder")
