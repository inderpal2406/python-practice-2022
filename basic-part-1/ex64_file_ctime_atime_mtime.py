"""Module to get creation, access and modification time for a file"""

# This script will print the ctime, atime and mtime of a file.
# In Windows, ctime would be creation time for the path.
# In Unix, ctime would be the time of last metadata change.
# atime is the time of last access of path.
# mtime is the time of last modification of path.
# The above timestamps will be checked for a test file test.txt.
# This file should exist in same directory as this script.
# If the file doesn't exist, then the script would create it.

# Import modules.

import platform
import sys
import os
import datetime
import clear_screen_module

# Define functions.

def main():
    """First function to be called"""
    # Clear screen using module function.
    clear_screen_module.clear_screen()
    print("This script prints ctime, atime and mtime of test.txt file.\n")
    # Decide filepath of test.txt as per the OS.
    if platform.system() == "Windows":
        filepath = ".\\test.txt"
    elif platform.system() == "Linux":
        filepath = "./test.txt"
    else:
        print("Script is designed for Windows & Linux Os only. Exiting now!")
        sys.exit(1)
    # If file test.txt doesn't exist, then create it.
    if not os.path.exists(filepath):
        fileobj = open(filepath,"w")
        fileobj.close()
        print("File test.txt didn't exist before & is now created.")
    else:
        print("File test.txt already exists.")
    # Calculate ctime, atime & mtime of test.txt file.
    ctime_epoch = os.path.getctime(filepath)
    atime_epoch = os.path.getatime(filepath)
    mtime_epoch = os.path.getmtime(filepath)
    ctime = datetime.datetime.fromtimestamp(ctime_epoch).strftime("%d-%m-%Y %H:%M:%S")
    atime = datetime.datetime.fromtimestamp(atime_epoch).strftime("%d-%m-%Y %H:%M:%S")
    mtime = datetime.datetime.fromtimestamp(mtime_epoch).strftime("%d-%m-%Y %H:%M:%S")
    # Display results.
    if platform.system() == "Windows":  # For Windows, ctime is creation time.
        print(f"\nCreation time (ctime): {ctime}")
    else:   # For Linux, ctime is last metadata change time.
        print(f"\nLast metadata change time (ctime): {ctime}")
    print(f"Last access time (atime): {atime}")
    print(f"Last modification time (mtime): {mtime}\n")
    return None

# Call main function when this script is executed.

if __name__ == "__main__":
    main()
