"""Module to find smallest number in a list"""

# Import modules.

import sys
import clear_screen_module

# Define functions.

def acceptlist():
    """Function to accept user integers & store them in list"""
    numlist = []
    index = 0
    try:
        count = int(input("How many integers will you provide: "))
        while index < count:
            num = int(input("Enter the integer: "))
            numlist.append(num)
            index = index + 1
    except ValueError:
        print("Please enter an integer value ony. Exiting script now!")
        sys.exit(1)
    return numlist

def main():
    """First function to be called"""
    clear_screen_module.clear_screen()
    print("This script accepts integers and displays the smallest one in them.\n")
    intlist = acceptlist()
    intlist.sort()
    print(f"The smallest integer is: {intlist[0]}")

# Call main() if the script is executed.

if __name__ == "__main__":
    main()
