import os
import subprocess

GREEN = "\033[32m"

_username_ = os.getenv("USERNAME")

while True:
    _input_ = input(f"{GREEN}Input an command [vpr, cli, ext] >>>   ")
    if _input_[:3] == "cli":
        subprocess.Popen(["start", "", f"C:\\Users\\{_username_}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\SecureAV-CLI.exe"], shell=True)
        print()
    if _input_[:3] == "vpr":
        subprocess.Popen(["start", "", f"C:\\Users\\{_username_}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Autostart\\SecureAV-VirusScan.exe"], shell=True)
        print()
    if _input_[:3] == "ext":
        break
    