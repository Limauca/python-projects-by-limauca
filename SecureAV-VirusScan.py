import os

GRAY = "\033[30m"
PURPLE = "\033[35m"
BLUE = "\033[34m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RESET = "\033[0m"

folders_to_scan = [
    os.path.join(os.path.expanduser("~"), "Downloads"),
    os.path.join(os.path.expanduser("~"), "Documents"),
    os.path.join(os.path.expanduser("~"), "Pictures"),
    os.path.join(os.path.expanduser("~"), "Desktop"),
    os.path.join(os.path.expanduser("~"), "Music"),
]

file_extensions = [
    '.exe', '.bat', '.cmd', '.com', '.scr', '.pif',
    '.vbs', '.js', '.jse', '.wsf', '.wsh', '.ps1', '.sh', '.py', '.rb', '.pl', '.hta',
    '.docm', '.xlsm', '.pptm', '.dotm', '.xltm',
    '.zip', '.rar', '.7z', '.tar', '.gz',
    '.iso', '.img',
    '.lnk', '.url',
    '.dll', '.sys', '.ocx',
    '.html', '.htm', '.pdf', '.crdownload'
]

def scan_folders(folders, extensions):
    found_files = []
    for folder in folders:
        if os.path.exists(folder):
            print(f"Scanning {folder}...")
            for root, dirs, files in os.walk(folder):
                for file in files:
                    if any(file.lower().endswith(ext) for ext in extensions):
                        found_files.append(os.path.join(root, file))
        else:
            print(f"Folder {folder} does not exist.")
    return found_files

def load_previous_scan(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            return set(line.strip() for line in f.readlines())
    return set()

def save_scan_results(file_path, found_files):
    with open(file_path, 'w') as f:
        for file in found_files:
            f.write(f"{file}\n")

def display_new_files(new_files):
    if new_files:
        print(GREEN, "\nFound new potentially malicious files:")
        for file in new_files:
            print("     ", file)
        print(RED, "It is advised to remove any files that you may not have downloaded or do not recognize.", RESET)
    else:
        print(YELLOW, "No new files were found.", RESET)


appdata_path = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'scanned_files.txt')

previously_found_files = load_previous_scan(appdata_path)

found_files = scan_folders(folders_to_scan, file_extensions)

new_files = set(found_files) - previously_found_files

display_new_files(new_files)

save_scan_results(appdata_path, found_files)

while True:
    if input("Enter 'exit' to exit:     ").strip().lower() == "exit":
        break