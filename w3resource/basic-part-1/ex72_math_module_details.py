"""Module to display details of math module"""

# This script will show functions available under math module
# and complete help (detailed info of each function) for math module.
# User will be asked if he wants to see only the available functions
# or complete help on math module.

# Import modules.

import math
import clear_screen_module
import sys
import time

# Define functions.

def main():
    """First function to be called"""
    # Clear screen using module function.
    clear_screen_module.clear_screen()
    print('''
    What details about math module do you want to see?
    a) Only functions of math module.
    b) Complete help documentation on math module.
    ''')
    user_choice = input("Enter your choice [a|b]: ")
    # Validate user input else exit.
    if user_choice.lower() not in ["a","b"]:
        print("\nInvalid input. Please enter [a|b]. Exiting script!\n")
        sys.exit(1)
    # Display output as per user choice.
    if user_choice.lower() == "a":
        print("\nFunctions under math module are as below:\n")
        print(f"{dir(math)}")
    else:
        print("\nPress q to exit help menu.\n")
        time.sleep(2)
        help(math)
    return None

# Call main function if the script is executed.

if __name__ == "__main__":
    main()
