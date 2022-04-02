"""Module to calculate sum of digits in an integer"""

# This script accepts an integer from user and then calculates sum of
# its digits.

# Import modules.

import sys
import clear_screen_module

# Define functions.

def sum_of_digits(num):
    """Function to calculate sum of digits of an integer"""
    if num == 0:
        return 0
    else:
        ans = 0
        while num != 0:
            rem = num % 10
            ans = ans + rem
            num = num // 10
        return ans

def main():
    """First function to be called"""
    # Clear screen using module function.
    clear_screen_module.clear_screen()
    print("This script calculates sum of digits of an integer number.\n")
    # Accept integer only from user using try-except.
    # Exit script if non-integer value is provided.
    try:
        user_int = int(input("Enter integer: "))
    except ValueError:
        print("Non-integer value provided. Exiting script now!")
        sys.exit(1)
    # Convert to positive integer if negative value provided.
    user_int = abs(user_int)
    # Call function to calculate sum of digits.
    our_sum = sum_of_digits(user_int)
    print(f"\nSum of digits of the number {user_int} is: {our_sum}\n")
    return None

# Call main() function when this script is executed.

if __name__ == "__main__":
    main()
