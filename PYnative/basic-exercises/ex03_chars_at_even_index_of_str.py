"""Module to print characters at even index of a string"""

# Import modules.

import clear_screen_module

# Define functions.

def main():
    """First function to be called"""
    clear_screen_module.clear_screen()
    print("This script prints chars at even indexes of a string.\n")
    userstr = input("Enter the string: ")
    print(f"\nOriginal string is: {userstr}")
    print("Printing only even index chars,")
    index = 1
    while index < len(userstr):
        print(userstr[index:index+1])
        index = index + 2

# Call main() when the script is executed.

if __name__ == "__main__":
    main()
    