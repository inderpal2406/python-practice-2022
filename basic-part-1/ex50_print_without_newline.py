"""Printing without newline"""
# This script will print a pattern of * in multiple iterations
# without introducing newline in each iteration.

# Import modules.

import clear_screen_module

# Define functions.

def main():
    """First function to be called"""
    # Clear the screen by using module function.
    clear_screen_module.clear_screen()
    # Print purpose of the script.
    print("This script will print * multiple times in single line.\n")
    print("The pattern is as below,\n")
    # Need to take upper limit as 6 in range() to get upto 5 if started from 1.
    for i in list(range(1,6,1)):    #pylint: disable=unused-variable
        # Modify end parameter to be empty instead of default new line.
        print("*",end="")
    print() # To bring cursor to new line after completion of the loop.
    print("That's it for now.")
    return None

# Call the main function if this script is executed.
if __name__ == "__main__":
    main()
