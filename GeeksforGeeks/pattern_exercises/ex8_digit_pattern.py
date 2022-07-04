"""Module to print digit pattern"""

# Import modules.

import sys
import clear_screen_module

# Define functions.

def digit_pattern(intnum):
    """Function to print digit pattern for intnum"""
    strnum = str(intnum)
    for eachstr in strnum:
        index = 1
        while index <= int(eachstr):
            print("*", end="")
            index = index + 1
        print()

def main():
    """First function to be called"""
    clear_screen_module.clear_screen()
    print("This script accepts a multi-digit integer & prints each digit's pattern.\n")
    try:
        userint = int(input("Enter the multi-digit integer number: "))
    except ValueError:
        print("Please enter an integer value only. Exiting script now!\n")
        sys.exit(1)
    if userint == 0:
        print("No pattern for integer 0.\n")
    elif userint < 0:
        print("No pattern for negative integer.\n")
    elif userint > 9999999999:
        print("The entered number is too big to print the pattern.\n")
    else:
        print(f"The pattern for integer {userint} is:\n")
        digit_pattern(userint)
    print() # Leave a line at the end of pattern.

if __name__ == "__main__":
    main()
