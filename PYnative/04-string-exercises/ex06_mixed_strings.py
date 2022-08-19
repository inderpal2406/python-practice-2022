"""Module to create a mixed string of 2 different strings by following matching rule"""

# Import modules.

import sys
import clear_screen_module

# Define functions.

def reversestr(fnstr):
    """Function to reverse a string"""
    charlist = []
    for eachchar in fnstr:
        charlist.append(eachchar)
    charlist.reverse()
    fnstrrev = ''.join(charlist)
    return fnstrrev

def mixstr(fnstr1,fnstr2):
    """Function to mix the strings"""
    fnstr1len = len(fnstr1)
    fnstr2len = len(fnstr2)
    if fnstr1len != fnstr2len:
        print("""
        The two strings are of unequal length. So, they are not suitable
        for this operation. Hence, exiting script now!
        """)
        sys.exit(1)
    fnstr2rev = reversestr(fnstr2)
    fnmixedstr = ""
    for index in range(0,fnstr1len,1):
        fnmixedstr = fnmixedstr + fnstr1[index] + fnstr2rev[index]
    return fnmixedstr

def main():
    """First function to be called"""
    clear_screen_module.clear_screen()
    print("""
    This script creates a mixed string of 2 different strings by matching first
    char of one string with last char of other string and so on.
    Press ENTER to proceed.
    """)
    input()
    str1 = "table"
    str2 = "maple"
    mixedstr = mixstr(str1,str2)
    print(f"String 1: {str1}\nString 2: {str2}\nMixed string: {mixedstr}\n")

# Call main() when the script is executed.

if __name__ == "__main__":
    main()
