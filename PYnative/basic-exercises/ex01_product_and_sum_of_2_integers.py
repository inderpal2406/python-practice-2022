"""Module to calculate product & sum of 2 integers"""

# Import modules.

import sys
import clear_screen_module

# Define functions.

def main():
    """First function to be called"""
    clear_screen_module.clear_screen()
    print('''
    This script accepts 2 integers & then,
    a) Displays their product if the product is less than 1000.
    b) Else displays their sum.
    ''')
    try:
        int1 = int(input("Enter first integer: "))
        int2 = int(input("Enter second integer: "))
    except ValueError:
        print("Please enter an integer value only. Exiting script now!\n")
        sys.exit(1)
    product = int1 * int2
    if product > 1000:
        addsum = int1 + int2
        print(f"The sum of integers is: {addsum}\n")
    else:
        print(f"The product of integers is: {product}\n")

# Call main() when the script is executed.

if __name__ == "__main__":
    main()
