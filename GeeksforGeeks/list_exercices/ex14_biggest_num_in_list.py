"""Module to find biggest integer in a list"""

# Import modules.

import clear_screen_module
import custom_list_functions

# Define functions.

def main():
    """First function to be called"""
    clear_screen_module.clear_screen()
    print("This script accepts integers & displays the largest in them.\n")
    numlist = custom_list_functions.accept_ints_in_list()
    if bool(numlist):
        numlist.sort()
        print(f"The largest integer is: {numlist[-1]}\n")
    else:
        print("Largest integer cannot be found with no input provided.\n")

# Call main() if the script is executed.

if __name__ == "__main__":
    main()
