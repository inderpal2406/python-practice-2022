"""Module to create a string from first, middle & last chars of another string"""

# Import modules.

import sys
import clear_screen_module

# Define functions.

def first_middle_last_char_str(fn_str1):
    """Function to create str from first, middle & last char of another str"""
    strlen = len(fn_str1)
    if strlen%2 == 0:
        print("Middle character couldn't be found as it is an even length string.")
        print("Hence, exiting script now!\n")
        sys.exit(1)
    else:
        midindex = strlen//2
        charlist = []
        charlist.append(fn_str1[0])
        charlist.append(fn_str1[midindex])
        charlist.append(fn_str1[-1])
        fn_ansstr = ''.join(charlist)
        return fn_ansstr

def main():
    """First function to be called"""
    clear_screen_module.clear_screen()
    print("""
    This script creates a string from first, middle, last characters of
    another string. Press ENTER to proceed.
    """)
    input()
    str1 = "James"
    ansstr = first_middle_last_char_str(str1)
    print(f"The string is: {str1}")
    print(f"String formed from first, middle & last characters is: {ansstr}\n")

if __name__ == "__main__":
    main()
