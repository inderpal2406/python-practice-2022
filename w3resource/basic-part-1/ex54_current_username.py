"""Display current user name"""

# Script to display current user name as per the OS type.

# Import modules.

import platform
import os
import sys
import clear_screen_module

# Define functions.

def main():
    """First function to be called"""
    # Clear screen using module function.
    clear_screen_module.clear_screen()
    print("This script prints current user name.\n")
    if platform.system() == "Windows":
        print(f"Current user: {os.environ['USERNAME']}\n")
    elif platform.system() == "Linux":
        print(f"Current user: {os.environ['USER']}\n")
    else:
        print("This script is designed for Windows & Linux OS only. Exiting now!")
        sys.exit(1)
    return None

# Call main() function when this script is executed.

if __name__ == "__main__":
    main()
