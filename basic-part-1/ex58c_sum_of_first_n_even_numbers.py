"""Calculate sum of first n even numbers"""

# This script will accept integer n from user.
# Then calculate sum of first n even numbers.

# Import modules.

import sys
import clear_screen_module

# Define functions.

def sum_of_n_even_nums(i):
    """Calculate sum of first i even numbers"""
    count = i
    num = 0
    ans = 0
    iterator = 1
    while iterator <= count:
        if num % 2 == 0:
            ans = ans + num
            iterator = iterator + 1
            num = num + 1
        else:
            num = num + 1
    return ans

def main():
    """First function to be called"""
    # Clear the screen.
    clear_screen_module.clear_screen()
    # Display purpose of the script.
    print("This script will calculate sum of first n even numbers.\n")
    # Accept n as an integer only from user using try-except block.
    try:
        n = int(input("Enter n: "))
    except ValueError:
        print("This script accepts only integer value for n. Exiting script!")
        sys.exit(1)
    n = abs(n)  # Converting n to positive value if negative value given.
    # Call function to calculate sum of first n even numbers.
    our_sum = sum_of_n_even_nums(n)
    print(f"\nThe sum of first {n} even numbers is: {our_sum}\n")
    return None

# Call main function if this script is executed.

if __name__ == "__main__":
    main()
