"""Module to check if a file is empty or not"""

# Import modules.

import os
import sys
import clear_screen_module

# Define functions.

def checkifempty(fn_txtfile):
    """Function to check if the file is empty"""
    if not os.path.exists(fn_txtfile):
        print(f"The path {fn_txtfile} doesn't exist. Exiting script now!\n")
        sys.exit(1)
    elif not os.path.isfile(fn_txtfile):
        print(f"The path {fn_txtfile} is not a file. Exiting script now!\n")
        sys.exit(1)
    else:
        fileobj = open(fn_txtfile,"r")
        content_list = fileobj.readlines()
        fileobj.close()
        if len(content_list) == 0:
            print(f"The file {fn_txtfile} is an empty file.\n")
        else:
            print(f"The file {fn_txtfile} is not an empty file.\n")

def main():
    """First function to be called"""
    clear_screen_module.clear_screen()
    txtfile = "txt-files\\empty.txt"
    print(f"This script will check if the file {txtfile} is empty or not.")
    print("Press ENTER to proceed.")
    input()
    checkifempty(txtfile)

# Call main() when the script is executed.

if __name__ == "__main__":
    main()
