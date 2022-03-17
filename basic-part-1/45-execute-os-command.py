# This script will detect the OS type and then execute the OS commands as per the OS type.

# Import modules.

import platform
import os

# Define functions.

def clear_screen():
    # Define global variable to be accessed in other function.
    global os_name
    os_name = platform.system()
    if os_name == "Windows":
        os.system("cls")
    elif os_name == "Linux":
        os.system("clear")
    else:
        print(f"This script is designed only for Windows and Linux OS. The OS on this system is neither Windows or Linux. Hence, exiting script!")
        exit(1)
    return None

def display_content():
    print(f"The content of current directory is as below,\n")
    if os_name == "Windows":
        os.system("dir")
    else:   # We use else as we are sure that this is for Linux. Otherwise the script would have exited in prev fn if OS was not Linux.
        os.system("ls")
    return None

def main():
    # Clear the screen as per the OS type.
    clear_screen()
    # Display the content of the current directory using the OS command.
    display_content()
    return None

# Main code starts here.

if __name__ == "__main__":
    main()
