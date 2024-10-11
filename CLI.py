import subprocess
import platform
import os

PU = "\033[35m"
BL = "\033[34m"
RE = "\033[31m"
GR = "\033[32m"
YE = "\033[33m"
WH = "\033[0m"

Color = WH

os_type = platform.system()
_username_ = os.getenv("USERNAME")
_run_ = True
if os_type == "Windows":
    _currentpath_ = "C:\\"
elif os_type == "Darwin":
    _currentpath_ = "/"

while _run_:
    _input_ = input(f"CLI > {_currentpath_} >>>  ").strip()
    if _input_[:4] == "help":
        if _input_[5:9] == "help":
            print("     Syntax: help <optional: command> [brings up a list of commands]")
        if _input_[5:9] == "txte":
            print("     Syntax: txte <optional: file name or path> [opens the native text editor]")
        if _input_[5:9] == "exit":
            print("     Syntax: exit <optional: skip confirmation [sc]> [exits the CLI]")
        if _input_[5:9] == "open":
            print("     Syntax: open <file path> [opens a file from a path]")
        if _input_[5:9] == "calc":
            print("     Syntax: calc <expression> [calculates a mathematical expression]")
        if _input_[5:9] == "diry":
            print("     Syntax: diry <optional: directory> [prints the directories inside of the current one or a stated directory]")
        if _input_[5:9] == "cdir":
            print("     Syntax: cdir <directory> [changes the current directory]")
        if _input_[5:9] == "cler":
            print("     Syntax: cler  [clears the interface]")
        else:
            print("Commands: \n     cler  [clears the interface] \n     cdir <directory> [changes the current directory] \n     diry <optional: directory> [prints the directories inside of the current one or a stated directory] \n     help <optional: command> [brings up a list of commands] \n     calc <expression> [calculates a mathematical expression] \n     txte <optional: file name or path> [opens the native text editor] \n     exit <optional: skip confirmation [sc]> [exits the CLI] \n     open <file path> [opens a file from a path]")
    
    if _input_[:4] == "calc":
        expr = _input_[5:]
        print(eval(expr))
        
    if _input_[:4] == "txte":
        if len(_input_) > 4:
            _filename_ = _input_[5:]
        if os_type == "Windows":
            _filepath_ = rf"C:\Users\{_username_}\Documents\{_filename_}"
        elif os_type == "Darwin":
            _filepath_ = rf"/Users/{_username_}/Documents/{_filename_}"
        elif os_type == "Linux":
            _filepath_ = rf"/home/{_username_}/Documents/{_filename_}"
        if len(_input_) > 4:
            if os_type == "Windows" and _input_[5:8] == "C:\\":
                _filepath_ = _input_[5:]
            elif os_type == "Darwin" and _input_[5] == "/":
                _filepath_ = _input_[5:]
            elif os_type == "Linux" and _input_[5] == "/":
                _filepath_ = _input_[5:]
        if not os.path.exists(_filepath_):
            with open(_filepath_, 'w') as f:
                f.write("")
        if os_type == "Windows":
            subprocess.Popen(["notepad.exe", _filepath_])
        elif os_type == "Darwin":
            subprocess.Popen(["open", "-a", "TextEdit", _filepath_])
        elif os_type == "Linux":
            subprocess.Popen(["gedit", _filepath_])
        
    if _input_[:4] == "exit":
        if not _input_[5:7] == "sc":
            _askexit_ = input("CLI >>> Do you rally want to exit?:  ").strip().lower()
        else:
            _askexit_ = "y"
        if _askexit_[0] == "y":
            _run_ = False

    if _input_[:4] == "open":        
        if os_type == "Windows":
            if _input_[5:8] == "C:\\":
                _filepath_ = _input_[5:]
                subprocess.Popen(["start", "", _filepath_], shell=True)
            if _input_[5:9] == "txte":
                _filepath_ = _input_[10:]
                subprocess.Popen(["notepad.exe", _filepath_])
        elif os_type == "Darwin":
            if _input_[5] == "/":
                subprocess.Popen(["open", _filepath_])
            if _input_[5:9] == "txte":
                _filepath_ = _input_[10:]
                subprocess.Popen(["open", "-a", "TextEdit", _filepath_])
        elif os_type == "Linux":
            if _input_[5] == "/":
                subprocess.Popen(["xdg-open", _filepath_])
            elif _input_[5:9] == "txte":
                _filepath_ = _input_[10:]
                subprocess.Popen(["gedit", _filepath_])
    
    if _input_[:4] == "diry":
        print()
        if not len(_input_) > 4:
            for item in os.listdir(_currentpath_):
                if os.path.isdir(os.path.join(_currentpath_, item)):
                    print(f"Directory: {item}")
                else:
                    print(f"File: {item}")
        else:
            _path_ = _input_[5:]
            for item in os.listdir(_path_):
                if os.path.isdir(os.path.join(_currentpath_, item)):
                    print(f"Directory: {item}")
                else:
                    print(f"File: {item}")
        
    if _input_[:4] == "cdir":
        path_input = _input_[5:].strip()
        if os.path.isabs(path_input):
            new_directory = path_input
        else:
            new_directory = os.path.join(_currentpath_, path_input)
        try:
            os.chdir(new_directory)
            _currentpath_ = os.getcwd()
            print(f"Changed directory to: {_currentpath_}")
        except FileNotFoundError:
            print(f"Error: The directory '{new_directory}' does not exist.")
        except PermissionError:
            print(f"Error: Permission denied to access '{new_directory}'.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")
    
    if _input_[:4] == "cler":
        if os_type == "Windows":
            os.system("cls")
        else:
            os.system("clear")
        