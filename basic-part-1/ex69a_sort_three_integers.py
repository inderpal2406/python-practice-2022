"""Module to sort three integers without using conditional statements and loops"""

# This script will accept 3 integers from the user and then sort them
# without using conditional statements and loops.

# Import modules.

import sys
import clear_screen_module

# Define functions.

def main():
    """First function to be called"""
    # Clear screen using module function.
    clear_screen_module.clear_screen()
    print("This script will accept 3 integers and then sort them.\n")
    # Define empty list to hold user input.
    user_input = []
    # Accept the three integers. Exit script if non-int value is provided.
    # We use loop to accept 3 integers.
    num = 1
    while num <= 3:
        try:
            user_num = int(input("Enter integer: "))
        except ValueError:
            print("Non-interger value provided. Exiting script now!")
            sys.exit()
        user_input.append(user_num)
        num = num + 1
    # Sort the input numbers in ascending order.
    user_input.sort()
    print(f"\nSorted output: {user_input}\n")
    #sorted_output = user_input.sort()  # It gets stored in None
    #print(f"The sorted output: {sorted_output}") # None gets displayed.
    # This could be because sort sorts and modifies exiting list itself.
    # As lists are mutable objects. When executed from console, it doesn't
    # give any output but modifes existing script. This existing script
    # needs to be printed again to view sorted numbers.
    return None

if __name__ == "__main__":
    main()
