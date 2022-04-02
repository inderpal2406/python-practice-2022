"""Print environment variables"""

# Script will print environment variables as per the OS type.

# Import modules.

import platform
import os
import clear_screen_module

# Define functions.

def main():
    """First function to be called"""
    # Clear screen using module function.
    clear_screen_module.clear_screen()
    print("This script prints environment variables.\n")
    print("Below values are taken from environment variables,\n")
    if platform.system() == "Windows":
        print(f"Computer name: {os.environ['COMPUTERNAME']}")
        print(f"User name: {os.environ['USERNAME']}")
        print(f"User home directory: {os.environ['HOMEDRIVE']}{os.environ['HOMEPATH']}\n")
    elif platform.system() == "Linux":
        print(f"Computer name: {os.environ['HOSTNAME']}")
        print(f"User name: {os.environ['USER']}")
        print(f"User home directory: {os.environ['HOME']}\n")
    return None

# Call main function when this script is executed.

if __name__ == "__main__":
    main()
