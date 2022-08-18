"""Module to create a str of first, middle & last chars of each input string"""

# This script implements different logic of concatenating the strings as compared
# to the script ex03c.

# Import modules.

import sys
import clear_screen_module

# Define functions.

def create_str_from_first_middle_last_chars(fn_strlist):
    """Function to create str of first, middle, last chars of each input str in strlist"""
    fn_ansstr = ""
    count = 1
    while count <= 3:
        if count == 1:
            for eachstr in fn_strlist:
                fn_ansstr = fn_ansstr + eachstr[0]
        elif count == 2:
            for eachstr in fn_strlist:
                strlen = len(eachstr)
                midindex = strlen // 2
                fn_ansstr = fn_ansstr + eachstr[midindex]
        else:
            for eachstr in fn_strlist:
                fn_ansstr = fn_ansstr + eachstr[-1]
        count = count + 1
    return fn_ansstr

def check_strlen_if_valid(fn_strlist):
    """Function to check if str length is odd, which is needed for this operation"""
    for eachstr in fn_strlist:
        strlen = len(eachstr)
        if strlen%2 == 0:
            print(f"\nLength of string {eachstr} is even. Only odd length strings needed.")
            print("Exiting script now!\n")
            sys.exit(1)

def main():
    """First function to be called"""
    clear_screen_module.clear_screen()
    print("""
    This script creates a string of first, middle & last characters of
    each of the input strings.
    """)
    userstr = input("Enter the strings with space between them [bob mob etc]: ")
    strlist = userstr.split()    # sep argument default value is a space.
    check_strlen_if_valid(strlist)
    ansstr = create_str_from_first_middle_last_chars(strlist)
    print(f"\nUser strings: {strlist}")
    print("String created from first, middle & last char of each user string is below,")
    print(f"{ansstr}\n")

if __name__ == "__main__":
    main()
