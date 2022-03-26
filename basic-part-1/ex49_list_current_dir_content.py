"""Module to do directory operations"""

# This script will list the current working directory and
# the number of files and directories in it and
# the files and directories in it.

# Import modules.

import os
import clear_screen_module

# Define functions.

def main():
    """Function containing all code"""
    # Call module function to clear the screen.
    clear_screen_module.clear_screen()
    # Print purpose of the script.
    print('''
    This script will print the below content,
    1. Current working directory
    2. Total number of files in the directory
    3. Files of the directory
    ''')
    print("Press ENTER key to proceed...")
    input() # Wait for ENTER key to be pressed.
    print(f"Current working directory: {os.getcwd()}\n")
    print(f"Number of files in directory: {len(os.listdir())}\n")
    print("The files are,\n")
    for each_file in os.listdir():
        print(f"{each_file}")
    return None

# Call the main function to execute the code.
if __name__ == "__main__":
    main()
