"""Module to put a new string in middle of another string"""

# Import modules.

import sys
import clear_screen_module

# Define functions.

def divide_str_and_place_new_str_in_middle(fn_str1,fn_str2):
    """Function to place a string in middle of another string"""
    str1len = len(fn_str1)
    if str1len%2 != 0:
        print(f"String 1: {fn_str1} is of odd length.")
        print("Only even length strings are suitable for this operation.")
        print("Hence, exiting script.\n")
        sys.exit(1)
    #mid = strlen / 2    # Gives answer in decimal. So, str1[0:mid] fails as mid is float num.
    midofstr = str1len // 2
    beforestr = fn_str1[0:midofstr]
    afterstr = fn_str1[midofstr:]
    strlist = []
    strlist.append(beforestr)
    strlist.append(fn_str2)
    strlist.append(afterstr)
    fn_ansstr = ''.join(strlist)
    return fn_ansstr

def main():
    """First function to be called"""
    clear_screen_module.clear_screen()
    print("This script puts string 2 in middle of string 1.")
    print("Press ENTER to proceed.\n")
    input()
    str1 = "Ault"
    str2 = "Kelly"
    ansstr = divide_str_and_place_new_str_in_middle(str1,str2)
    print(f"String 1: {str1}\nString 2: {str2}")
    print(f"Result string: {ansstr}\n")

if __name__ == "__main__":
    main()
