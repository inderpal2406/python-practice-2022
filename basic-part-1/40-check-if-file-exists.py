# This script will check if a file exists or not.
# This script can be executed on both Windows and Linux.

# Import modules.

import platform
import os

# Define functions.

def file_check_on_windows():
    # Clear the screen.
    os.system("cls")
    # Display the purpose of the script.
    print(f"This script will check if the file test.txt exists in C:\\Temp\\ directory.\n")
    # Check if the file exists.
    if os.path.exists("C:\\Temp\\test.txt"):
        print(f"The file C:\\Temp\\test.txt exists.")
    else:
        print(f"The file C:\\Temp\\test.txt doesn't exist.")
    return None

def file_check_on_linux():
    # Clear the screen.
    os.system("clear")
    # Display the purpose of the script.
    print(f"This script will check if the file test.txt exists in /tmp directory.\n")
    # Check if the file exists.
    if os.path.exists("/tmp/test.txt"):
        print(f"The file /tmp/test.txt exists.")
    else:
        print(f"The file /tmp/test.txt doesn't exist.")
    return None

def main():
    # Check if the OS is Linux or Windows.
    os_name = platform.system()
    if os_name == "Windows":
        file_check_on_windows()
    elif os_name == "Linux":
        file_check_on_linux()
    else:
        print(f"This script is designed to work only on Windows and Linux OS.")
        print(f"This script has a different OS. Hence, exiting script.")
        exit(1)
    return None

# Main code starts here.

if __name__ == "__main__":
    main()
