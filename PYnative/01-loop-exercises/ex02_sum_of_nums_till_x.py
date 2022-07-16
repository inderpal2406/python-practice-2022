"""Module to calculate sum of all numbers upto number x"""

# Import modules.

import sys
import clear_screen_module

# Define functions.

def CalculateSumOfNumsUptoX(fnnum):
    """Function to calculate sum of all nums upto num x"""
    fnsum = 0
    for eachnum in range(1,fnnum+1,1):
        fnsum = fnsum + eachnum
    return fnsum

def main():
    """First function to be called"""
    clear_screen_module.clear_screen()
    print("This script calculates sum of all numbers upto number x.\n")
    try:
        num = int(input("Enter the number x: "))
    except ValueError:
        print("Please enter an integer number only. Exiting script now.\n")
        sys.exit(1)
    if num < 0:
        print("Number cannot be less than 0. Exiting script now.\n")
        sys.exit(1)
    oursum = CalculateSumOfNumsUptoX(num)
    print(f"The sum of all numbers upto number {num} is: {oursum}\n")

# Call main() when the script is executed.

if __name__ == "__main__":
    main()
