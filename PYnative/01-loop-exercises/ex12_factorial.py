"""Module to calculate factorial of a number"""

# Import modules.

import clear_screen_module

# Define functions.

def calculate_factorial(fnnum):
    """Function to calculate factorial of a number"""
    index = 1
    product = 1
    while index <= fnnum:
        product = product * index
        index = index + 1
    return product

def main():
    """First function to be called"""
    clear_screen_module.clear_screen()
    print("This script calculates factorial of a given number.")
    print("Press ENTER to proceed.")
    input()
    num = 5
    factorialans = calculate_factorial(num)
    print(f"Factorial of {num} is: {factorialans}\n")

# Call main function when the script is executed.

if __name__ == "__main__":
    main()
