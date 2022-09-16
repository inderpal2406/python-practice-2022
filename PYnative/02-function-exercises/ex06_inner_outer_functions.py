"""Module to demonstrate inner & outer functions"""

# A function can be defined inside another function.

# Import modules.

import sys
import clear_screen_module

# Define functions.

def add_2_nums(num1,num2):
    """Outer function to add 5 to the sum returned by inner function"""
    def addition(int1,int2):
        """Inner function to add 2 nums"""
        sum_of_add = int1 + int2
        return sum_of_add
    fn_sum = addition(num1,num2)
    add_5_to_sum = fn_sum + 5
    return add_5_to_sum

def main():
    """First function to be called"""
    clear_screen_module.clear_screen()
    print("This script accepts 2 integers and adds them.\n")
    try:
        int1 = int(input("Enter the first integer: "))
        int2 = int(input("Enter the second integer: "))
    except ValueError:
        print("This script accepts only integer values. Exiting script now!\n")
        sys.exit(1)
    oursum = add_2_nums(int1,int2)
    print(f"The sum of {int1}, {int2} & 5 is: {oursum}\n")

if __name__ == "__main__":
    main()
