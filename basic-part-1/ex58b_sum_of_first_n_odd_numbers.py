"""Calculate sum of first n odd numbers"""

# This script will accept n as user input.
# Then calculate sum of first n odd numbers.

# Import modules.

import sys
import clear_screen_module

# Define functions.

def sum_of_n_odd(i):
    """Function to calculate sum of first i odd numbers"""
    count = i
    num = 1
    ans = 0
    iterator = 1
    while iterator <= count:
        if num % 2 == 1:
            ans = ans + num
            iterator = iterator + 1
            num = num + 1
        else:
            num = num + 1
    return ans

def main():
    """First function to be called"""
    # Clear screen using module function.
    clear_screen_module.clear_screen()
    # Display purpose of the script.
    print("This script will calculate sum of first n odd numbers.\n")
    # Accept n as integer only from the user using try-except.
    try:
        n = int(input("Enter n: "))
    except ValueError:
        print("This script accepts only integer value for n. Exiting script!")
        sys.exit(1)
    n = abs(n)  # Converting n to positive value if negative value given.
    our_sum = sum_of_n_odd(n)
    print(f"\nThe sum of first {n} odd numbers is: {our_sum}\n")
    return None

# Call main function if this script is executed.

if __name__ == "__main__":
    main()
