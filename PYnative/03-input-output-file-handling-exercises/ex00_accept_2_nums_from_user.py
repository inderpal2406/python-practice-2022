"""Module to accept 2 nums from user & perform their multiplication"""

# Import modules.

import sys
import clear_screen_module

# Define functions.

def calculateproduct(fn_num1,fn_num2):
    """Function to calculate product of fn_num1 & fn_num2"""
    fn_product = fn_num1 * fn_num2
    # Round off to 2 digits after decimal point if many digits are present after decimal point.
    # If product is an int, then round() won't do anything & just return the normal int value.
    # round() is done on mixed numbers.
    fn_product = round(fn_product,2)
    return fn_product

def main():
    """First function to be called"""
    clear_screen_module.clear_screen()
    print("This script accepts 2 numbers and calculate their product.\n")
    try:
        num1 = eval(input("Enter num1: "))
        num2 = eval(input("Enter num2: "))
    except NameError:
        print("Please enter a numeric value only. Exiting script now!")
        sys.exit(1)
    # eval() accepts boolean values as well. So check for it.
    if type(num1) == bool or type(num2) == bool:
        print("Please enter a numeric value only. Exiting script now!")
        sys.exit(1)
    product = calculateproduct(num1,num2)
    print(f"Product of {num1} & {num2} is: {product}\n")

# Call main() when the script is executed.

if __name__ == "__main__":
    main()
