"""Module to reverse a string"""

# Import modules.

import clear_screen_module

# Define functions.

def reversethestr(inputstr):
    """Function to reverse a string"""
    strlist = []
    index = 0
    while index < len(inputstr):
        strlist.append(inputstr[index])
        index = index + 1
    strlist.reverse()
    ansstr = ''.join(strlist)
    return ansstr

def main():
    """First function to be called"""
    clear_screen_module.clear_screen()
    print("This script reverses the provided string.\n")
    userstr = input("Enter the string: ")
    reversestr = reversethestr(userstr)
    print(f"\nThe entered string is: {userstr}")
    print(f"The reversed string is: {reversestr}\n")

# Call main() when the script is executed.

if __name__ == "__main__":
    main()
