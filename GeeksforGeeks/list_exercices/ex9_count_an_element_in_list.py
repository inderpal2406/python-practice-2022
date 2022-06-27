"""Module to count an element in list"""

import sys
import clear_screen_module

def main():
    """First function to be called"""
    clear_screen_module.clear_screen()
    print("This script will count an element in a list.\n")
    numlist = [1,2,7,1,5,2,5,6,9,5]
    print(f"The list is: {numlist}")
    try:
        userinput = int(input("Enter the number to be counted: "))
    except ValueError:
        print("Please enter an integer only. Exiting script now!")
        sys.exit(1)
    count = numlist.count(userinput)
    print(f"\nThe number {userinput} occurs {count} number of times in list.\n")

if __name__ == "__main__":
    main()
