"""Module to check if element exists in a list"""

# Import modules.

import sys
import clear_screen_module

# Define functions.

def main():
    """First function to be called"""
    clear_screen_module.clear_screen()
    print("This script checks if an element exists in the list.\n")
    numlist = [1,2,3,4,5]
    print(f"The list is: {numlist}\n")
    try:
        userinput = int(input("Enter the number: "))
    except ValueError:
        print("Please enter an integer only. Exiting script!")
        sys.exit(1)
    if userinput in numlist:
        print(f"The number {userinput} exists in the list.\n")
    else:
        print(f"The number {userinput} doesn't exist in the list.\n")
    return None

# Call main() when the script is executed.

if __name__ == "__main__":
    main()
