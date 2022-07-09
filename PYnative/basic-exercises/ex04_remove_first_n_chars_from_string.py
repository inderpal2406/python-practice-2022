"""Module to remove first n chars from a string"""

# Import modules.

import sys
import clear_screen_module

# Define functions.

def removenchars(ourstr,num):
    """Function to remove first num chars from ourstr"""
    resultstr = ourstr[num:]
    return resultstr

def main():
    """First function to be called"""
    clear_screen_module.clear_screen()
    print("This script removes first n chars from a string.\n")
    userstr = input("Enter the string: ")
    try:
        noofchars = int(input("Enter n: "))
    except ValueError:
        print("Please enter an integer value only for n. Exiting script now!\n")
        sys.exit(1)
    ansstr = removenchars(userstr,abs(noofchars))
    print(f"Original string: {userstr}")
    print(f"After removing first {noofchars} chars: {ansstr}\n")

if __name__ == "__main__":
    main()
