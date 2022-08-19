"""Module to print lower case letters first in a string"""

# Import modules.

import clear_screen_module

# Define functions.

def lower_chars_first(fnstr):
    """Function to rearrange lower case chars first in a string"""
    lowercharlist = []
    uppercharlist = []
    for eachchar in fnstr:
        ascii_code = ord(eachchar)
        if ascii_code in list(range(97,123,1)):
            lowercharlist.append(eachchar)
        if ascii_code in list(range(65,91,1)):
            uppercharlist.append(eachchar)
    loweransstr = ''.join(lowercharlist)
    upperansstr = ''.join(uppercharlist)
    ansstr = loweransstr + upperansstr
    return ansstr

def main():
    """First function to be called"""
    clear_screen_module.clear_screen()
    print("This script prints lower case letters first from a string.")
    print("Press ENTER to proceed.")
    input()
    ourstr = "PyNaTive"
    ansstr = lower_chars_first(ourstr)
    print(f"Our string: {ourstr}")
    print(f"Answer string: {ansstr}\n")

if __name__ == "__main__":
    main()
