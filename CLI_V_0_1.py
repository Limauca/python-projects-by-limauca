import subprocess
import platform
import os

def set_colour(index):
    return f"\033[38;5;{index}m"

colour = "\033[37m"

os_type = platform.system()
_username_ = os.getenv("USERNAME")
_run_ = True
if os_type == "Windows":
    _currentpath_ = "C:\\"
elif os_type == "Darwin":
    _currentpath_ = "/"

while _run_:
    _input_ = input(f"{colour}CLI > {_currentpath_} >>>  ").split()
    if _input_[0] == "help":
        if len(_input_) <= 2:
            if len(_input_) == 2:  
                if _input_[1] == "help":
                    print(f"{colour}      Syntax: help <optional: command> [brings up a list of commands]")
                if _input_[1] == "txte":
                    print(f"{colour}      Syntax: txte <optional: file name or path, optional: hlp [for help]> [opens the native text editor]")
                if _input_[1] == "exit":
                    print(f"{colour}      Syntax: exit <optional: skip confirmation [sc]> [exits the CLI]")
                if _input_[1] == "open":
                    print(f"{colour}      Syntax: open <file path> [opens a file from a path]")
                if _input_[1] == "calc":
                    print(f"{colour}      Syntax: calc <expression> [calculates a mathematical expression]")
                if _input_[1] == "dir":
                    print(f"{colour}      Syntax: dir <optional: directory> [prints the directories inside of the current one or a stated directory]")
                if _input_[1] == "cdir":
                    print(f"{colour}      Syntax: cdir <directory> [changes the current directory]")
                if _input_[1] == "clear":
                    print(f"{colour}      Syntax: clear <optional: hlp [for help]> [clears the interface]")
            else:
                print(f"{colour}Commands: \n     cler  [clears the interface] \n     cdir <directory> [changes the current directory] \n     diry <optional: directory> [prints the directories inside of the current one or a stated directory] \n     help <optional: command> [brings up a list of commands] \n     calc <expression> [calculates a mathematical expression] \n     txte <optional: file name or path> [opens the native text editor] \n     exit <optional: skip confirmation [sc]> [exits the CLI] \n     open <file path> [opens a file from a path]\n")
        else:
            print(f"{colour}\n       ERROR: Expected one or two arguments, recieved {len(_input_)}.\n")

    if _input_[0] == "calc":
        if len(_input_) > 1:
            expr = "".join(_input_[1:])
            try:
                _result_ = eval(expr)
                print(_result_)
            except Exception as e:
                print(f"{colour}\n      ERROR, invalid expression: {e}\n")
                continue
        else:
            print(f"{colour}\n     Syntax: calc <expression> [calculates a mathematical expression]\n")
    
    if _input_[0] == "exit":
        if len(_input_) == 1:
            _askexit_ = input(f"{colour}CLI >>> Do you really want to exit?:  ").strip().lower()
        elif _input_[1] == "sc":
            _askexit_ = "y"
        if _askexit_[0] == "y":
            print("\033[37m")
            _run_ = False

    if _input_[0] == "open":
        if len(_input_) > 1:
            if len(_input_) > 2:
                _inputstr_ = "".join(_input_[2:])
            if len(_input_) == 2:
                _inputstr_ = "".join(_input_[1:])
            if os_type == "Windows":
                _filepath_ = _inputstr_
                if _inputstr_[0:3] == "C:\\":
                    try:
                        subprocess.Popen(["start", "", _filepath_], shell=True)
                    except Exception as e:
                        print(f"{colour}\n      ERROR, file could not be found: {e}.\n")
                if _input_[1] == "txte":
                    try:
                        subprocess.Popen(["notepad.exe", _filepath_])
                    except Exception as e:
                        print(f"{colour}\n       ERROR, file could not be found: {e}.\n")
            elif os_type == "Darwin":
                _filepath_ = _inputstr_
                if _inputstr_[0] == "/":
                    try:
                        subprocess.Popen(["open", _filepath_])
                    except Exception as e:
                        print(f"{colour}\n       ERROR, file could not be found: {e}.\n")
                if _inputstr_[0:3] == "txte":
                    try:
                        subprocess.Popen(["open", "-a", "TextEdit", _filepath_])
                    except Exception as e:
                        print(f"{colour}\n      ERROR, file could not be found: {e}.\n")
            elif os_type == "Linux":
                _filepath_ = _inputstr_
                if _inputstr_[0] == "/":
                    try:
                        subprocess.Popen(["xdg-open", _filepath_])
                    except Exception as e:
                        print(f"{colour}\n      ERROR, file could not be found: {e}.\n")
                elif _inputstr_[0:3] == "txte":
                    try:
                        subprocess.Popen(["gedit", _filepath_])
                    except Exception as e:
                        print(f"{colour}\n      ERROR, file could not be found: {e}.\n")
        else:
            print(f"{colour}\n     Syntax: open <file path> [opens a file from a path]\n")

    if _input_[0] == "dir":
        print()
        if len(_input_) > 1:
            if _input_[1].strip() == "crnt":
                for item in os.listdir(_currentpath_):
                    if os.path.isdir(os.path.join(_currentpath_, item)):
                        print(f"{colour}      Directory: {item}")
                    else:
                        print(f"{colour}      File: {item}")
            else:
                _path_ = "".join(_input_[1:])
                for item in os.listdir(_path_):
                    if os.path.isdir(os.path.join(_currentpath_, item)):
                        print(f"{colour}      Directory: {item}")
                    else:
                        print(f"{colour}      File: {item}")
            print()
        else:
            print(f"{colour}\n     Syntax: dir <crnt [for the current directory], optional: directory> [prints the directories inside of the current one or a stated directory]\n")

    if _input_[0] == "clear":
        if len(_input_) > 1:
            if _input_[1] == "hlp":
                print(f"{colour}\n     Syntax: clear <optional: hlp [for help]> [clears the interface]\n")
        else:
            if os_type == "Windows":
                os.system("cls")
            else:
                os.system("clear")

    if _input_[0] == "cdir":
        if len(_input_) > 1:
            path_input = "".join(_input_[1:])
            if os.path.isabs(path_input):
                new_directory = path_input
            else:
                new_directory = os.path.join(_currentpath_, path_input)
            try:
                os.chdir(new_directory)
                _currentpath_ = os.getcwd()
                print(f"{colour}\n      Changed directory to: {_currentpath_}\n")
            except FileNotFoundError:
                print(f"{colour}\n      Error: The directory '{new_directory}' does not exist.\n")
            except PermissionError:
                print(f"{colour}\n      Error: Permission denied to access '{new_directory}'.\n")
            except Exception as e:
                print(f"{colour}\n      An error occurred: {str(e)}\n")
        else:
            print(f"{colour}\n     Syntax: cdir <directory> [changes the current directory]\n")
    
    if _input_[0] == "txte":
        if len(_input_) > 1:
            if _input_[1] == "hlp":
                print(f"{colour}\n     Syntax: txte <optional: file name or path, optional: hlp [for help]> [opens the native text editor]\n")
                continue
            _filename_ = _input_[1:].join()
        else:
            _filename_ = "unnamed.txt"
        if os_type == "Windows":
            _filepath_ = rf"C:\Users\{_username_}\Documents\{_filename_}"
        elif os_type == "Darwin":
            _filepath_ = rf"/Users/{_username_}/Documents/{_filename_}"
        elif os_type == "Linux":
            _filepath_ = rf"/home/{_username_}/Documents/{_filename_}"
        if len(_input_) > 1:
            if os_type == "Windows" and _input_[5:8] == "C:\\":
                _filepath_ = _input_[1:].join()
            elif os_type == "Darwin" and _input_[5] == "/":
                _filepath_ = _input_[1:].join()
            elif os_type == "Linux" and _input_[5] == "/":
                _filepath_ = _input_[1:].join()
        if not os.path.exists(_filepath_):
            with open(_filepath_, 'w') as f:
                f.write("")
        if os_type == "Windows":
            subprocess.Popen(["notepad.exe", _filepath_])
        elif os_type == "Darwin":
            subprocess.Popen(["open", "-a", "TextEdit", _filepath_])
        elif os_type == "Linux":
            subprocess.Popen(["gedit", _filepath_])

    if _input_[0] == "colour":
        if len(_input_) > 1:
            if _input_[1] == "ansi":
                if len(_input_) > 2:
                    try:
                        if 1 <= int(_input_[2]) <= 255:
                            colour = set_colour(int(_input_[1]))
                    except Exception as e:
                        print(f"{colour}\n      ERROR, invalid colour: {e}\n")
            if _input_[1] == "sgr":
                if len(_input_) > 2:
                    try:
                        if 30 <= int(_input_[2]) <= 37 or 90 <= int(_input_[2]) <= 97:
                            colour = f"\033[{_input_[2]}m"
                        else:
                            print(f"{colour}\n      ERROR, invalid colour, choose a number between 30 and 37 or 90 and 97")
                    except Exception as e:
                        print(f"{colour}\n      ERROR, invalid colour: {e}\n")
            if _input_[1] == "bckgr":
                if len(_input_) > 2:
                    try:
                        if 40 <= int(_input_[2]) <= 47 or 100 <= int(_input_[2]) <= 107:
                            colour = f"\033[{_input_[2]}m"
                        else:
                            print(f"{colour}\n      ERROR, invalid colour, choose a number between 40 and 47 or 100 and 107")
                    except Exception as e:
                        print(f"{colour}\n      ERROR, invalid colour: {e}\n")                        
        else:
            print()
    
    if _input_[0] == "colours":
        for i in range(1, 256):
            print(f"{set_colour(i)}      colour ANSI {i}")
        for i in range(30, 38):
            print(f"\033[{i}m      colour SGR {i}")
        for i in range(90, 98):
            print(f"\033[{i}m      colour SGR {i}")
        print()