"""Module to swap 2 list items"""

# Import modules.

import sys
import clear_screen_module

# Define functions.

def numinlist(num):
    """Check if num is present in list else exit script"""
    if num not in numlist:
        print(f"{num} is not present in the script. Exiting script!")
        sys.exit(1)
    return None

def main():
    """First function to be called"""
    clear_screen_module.clear_screen()
    print("This script will swap 2 list items.\n")
    global numlist
    numlist = [1,2,3,4,5]
    print(f"The given list is: {numlist}\n")
    try:
        num1 = int(input("Enter first number to be swapped: "))
        numinlist(num1)
        num2 = int(input("Enter second number to be swapped: "))
        numinlist(num2)
    except ValueError:
        print("Please enter integer value only. Exiting script!")
        sys.exit(1)
    num1index = numlist.index(num1)
    num2index = numlist.index(num2)
    numlist[num1index] = num2
    numlist[num2index] = num1
    print(f"\nThe list after swapping is: {numlist}\n")
    return None

# Call main() if the script is executed.

if __name__ == "__main__":
    main()
