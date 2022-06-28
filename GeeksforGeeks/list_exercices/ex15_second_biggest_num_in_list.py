"""Module to find second biggest integer in a list"""

# Import modules.

import clear_screen_module
import custom_list_functions

# Define functions.

def main():
    """First function to be called"""
    clear_screen_module.clear_screen()
    print("This script accepst integers & finds second biggest in them.\n")
    numlist = custom_list_functions.accept_ints_in_list()
    if bool(numlist):
        numlist.sort()
        print(f"The second biggest integer is: {numlist[-2]}\n")
    else:
        print("Second biggest integer cannot be found if no input is given.\n")

# Call main() when the script is executed.

if __name__ == "__main__":
    main()
