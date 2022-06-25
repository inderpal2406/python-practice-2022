"""Calculate sum of odd numbers upto number n"""

# This script will calculate sum of odd numbers upto number n.
# number n would be accepted from the user.

# Import modules.

import sys
import clear_screen_module

# Define functions.

def sum_of_odd_nums_upto_n(i):
    """Function for sum of odd nums upto n"""
    num = 1
    ans = 0
    while num <= i:
        if num % 2 == 1:
            ans = ans + num
        num = num + 1
    return ans

def main():
    """First function to be called"""
    # Clear screen using module function.
    clear_screen_module.clear_screen()
    # Display purpose of the script.
    print("This script will calculate sum of odd numbers upto number n.\n")
    # Accept integer n using try-except block.
    try:
        n = int(input("Enter n: "))
    except ValueError:
        print("This script accepts only integer value for n. Exiting script!")
        sys.exit(1)
    n = abs(n)  # Covert negative num to positive if user provides negative int.
    # Call function to calculate sum.
    our_sum = sum_of_odd_nums_upto_n(n)
    print(f"\nSum of odd numbers upto {n} is: {our_sum}\n")
    return None

# Call main function if this script is executed.

if __name__ == "__main__":
    main()
