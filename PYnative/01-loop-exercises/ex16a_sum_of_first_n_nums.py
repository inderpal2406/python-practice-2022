"""Module to calculate sum of first n numbers"""

# Import modules.

import sys
import clear_screen_module

# Define functions.

def CalculateSumUptoN(fn_num_n):
    """Function to calculate sum of numbers from 1 to fn_num_n"""
    fn_sum = 0
    for eachnum in range(1,fn_num_n+1,1):
        fn_sum = fn_sum + eachnum
    return fn_sum

def main():
    """First function to be called"""
    clear_screen_module.clear_screen()
    print("This script calculates sum of numbers from 1 to n.\n")
    try:
        num_n = int(input("Enter n: "))
    except ValueError:
        print("Please enter an integer number only. Exiting script now.\n")
        sys.exit(1)
    if num_n <= 0:
        print("Please enter an integer greater than zero. Exiting script now!\n")
        sys.exit(1)
    totalsum = CalculateSumUptoN(num_n)
    print(f"The sum of numbers from 1 to {num_n} is: {totalsum}\n")

# Call main() when the script is executed.

if __name__ == "__main__":
    main()
