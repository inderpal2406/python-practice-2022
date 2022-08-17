"""Module to read specific line from a file"""

# Import modules.

import os
import sys
import clear_screen_module

# Define functions.

def main():
    """First function to be called"""
    clear_screen_module.clear_screen()
    filepath = "txt-files\\test1.txt"
    linenum = 4
    print(f"This script reads line number {linenum} from file {filepath}")
    print("Press ENTER to proceed.")
    input()
    if not os.path.isfile(filepath):
        print(f"File {filepath} doesn't exist. Exitting script now!\n")
        sys.exit(1)
    fileobj = open(filepath,"r")
    content_list = fileobj.readlines()  # Empty line in the end is not read.
    fileobj.close()
    #print(content_list)
    if len(content_list) < linenum:
        print(f"File {filepath} has less than {linenum} number of lines. Exiting script!\n")
        sys.exit(1)
    count = 1
    for eachitem in content_list:
        if count == linenum:
            print(f"Line number {linenum} from file {filepath} is as below,")
            print(eachitem,"\n")
            break
        count = count + 1
    # Don't know why but below logic didn't work. Instead of this, logic of len(content_list)
    # being compared with linenum to be read is implemented at line 26 above.
    #if count < linenum:
        #print(f"File {filepath} has less than {linenum} number of lines.\n")

if __name__ == "__main__":
    main()
