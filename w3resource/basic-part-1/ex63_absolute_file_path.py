"""Module to get absolute file paths"""

# This script will print the absolute file paths of all the files
# in the current directory.

# Import modules.

import os
import clear_screen_module

# Define functions.

def list_abs_path_of_files(dirname):
    """Function to list absolute paths of files of desired directory"""
    # This function can be called elsewhere by importing parent module.
    # In such case, we need to chdir to required dir to list files.
    # Otherwise, os.listdir() would get the list of files, but
    # os.path.abspath() won't be able to locate files, as we call
    # function from another location.
    present_dir = os.getcwd()
    os.chdir(dirname)   # To locate files properly.
    files_list = os.listdir(dirname)
    for file in files_list:
        abs_path = os.path.abspath(file)
        print(f"{abs_path}")
    total_files = len(files_list)
    print(f"\nTotal number of files: {total_files}")
    os.chdir(present_dir)   # Again change dir from where function is called.
    return None

def main():
    """First function to be called"""
    # Clear the screen using module function.
    clear_screen_module.clear_screen()
    print("This script prints absolute paths of all files in current directory.\n")
    current_dir = os.getcwd()
    print(f"Current directory: {current_dir}\n")
    print("Files in current dir are as below with their absolute paths,\n")
    # Call function to list absolute paths of files.
    list_abs_path_of_files(current_dir)
    print("\nAll files are listed above.\n")
    return None

# Call main function if this script is executed.

if __name__ == "__main__":
    main()
