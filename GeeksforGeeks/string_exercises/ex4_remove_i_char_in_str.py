"""Module to remove i'th char in a string"""

# Import modules.

import sys
import clear_screen_module

# Define functions.

def removechar(inputstr,position):
    """Function to remove char at position of input string"""
    strlist = []
    index = 0
    while index < len(inputstr):
        strlist.append(inputstr[index])
        index = index + 1
    strlist.pop(position-1)
    ansstr = ''.join(strlist)
    return ansstr

def main():
    """First function to be called"""
    clear_screen_module.clear_screen()
    print("This script removes i'th letter in a string.\n")
    userstr = input("Enter the string: ")
    print(f"\nThe provided string has positions from 1 to {len(userstr)}")
    try:
        removeint = int(input("Enter the position of letter to be removed: "))
    except ValueError:
        print("\nPlease enter an integer value only. Exiting script now!\n")
        sys.exit(1)
    if removeint in range(1,len(userstr)+1,1):
        updatedstr = removechar(userstr,removeint)
        print(f"\nEntered string: {userstr}")
        print(f"String after removing character at position {removeint} is: {updatedstr}\n")
    else:
        print("\nThe provided position doesn't exist.\n")

# Call main() when the script is executed.

if __name__ == "__main__":
    main()
