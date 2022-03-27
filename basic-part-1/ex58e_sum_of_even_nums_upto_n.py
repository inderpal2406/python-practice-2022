"""Sum of even numbers upto number n"""

# This script will accept an integer number n from user.
# Then it'll calculate sum of even numbers upto number n.

# Import modules.

import sys
import clear_screen_module

# Define functions.

def sum_of_even_nums_upto_n(i):
    """Function for sum of even nums upto n"""
    num = 1
    ans = 0
    while num <= i:
        if num % 2 == 0:
            ans = ans + num
        num = num + 1
    return ans

def main():
    """First function to be called"""
    # Clear screen using module function.
    clear_screen_module.clear_screen()
    print("This script calculates sum of even numbers upto n.\n")
    # Accept only int value for n using try-except.
    try:
        n = int(input("Enter n: "))
    except ValueError:
        print("The script accepts only integer value for n. Exiting script!")
        sys.exit(1)
    n = abs(n)  # Covert to positive value if user enters negative int.
    # Call function to calculate sum.
    our_sum = sum_of_even_nums_upto_n(n)
    print(f"\nSum of even numbers upto {n} is: {our_sum}\n")
    return None

# Call main function if this script gets executed.

if __name__ == "__main__":
    main()
