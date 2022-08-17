"""Module to create a string of middle 3 characters of another string"""

# Import modules.

import sys
import time
import clear_screen_module

# Define functions.

def middle_3_chars_str(fn_str):
    """Function to create a str of middle 3 chars of fn_str"""
    strlen = len(fn_str)
    if strlen%2 == 0:
        print(f"The string {fn_str} is of even length.")
        print("Only odd length strings are suitable for this operation.")
        print("Hence, exiting script.\n")
        sys.exit(1)
    middleindex = strlen // 2
    beforemiddleindex = middleindex - 1
    aftermiddleindex = middleindex + 1
    charlist = []
    charlist.append(fn_str[beforemiddleindex])
    charlist.append(fn_str[middleindex])
    charlist.append(fn_str[aftermiddleindex])
    fn_resultstr = ''.join(charlist)
    return fn_resultstr

def main():
    """First function to be called"""
    clear_screen_module.clear_screen()
    print("This script creates a string of middle 3 chars of another string.")
    print("Press ENTER to proceed.")
    input()
    str1 = "JhonDipPeta"
    resultstr1 = middle_3_chars_str(str1)
    print(f"String: {str1}\nMiddle 3 characters' string: {resultstr1}\n")
    time.sleep(2)
    str2 = "JaSonAy"
    resultstr2 = middle_3_chars_str(str2)
    print(f"String: {str2}\nMiddle 3 characters' string: {resultstr2}\n")

# Call main() when the script is executed.

if __name__ == "__main__":
    main()
