"""Sum of first n numbers"""

# This script will calculate sum of first n numbers.
# n would be accepted from the user.

# Import modules.

import sys
import clear_screen_module

# Define functions.

def calculate_sum(i):
    """Function to calculate sum of first i numbers"""
    ans = 0
    for j in list(range(1,i+1,1)):
        ans = ans+j
    return ans

def main():
    """First function to be called"""
    # Clear the screen by using module function.
    clear_screen_module.clear_screen()
    # Display purpose of the script.
    print("This script will calculate sum of first n numbers.\n")
    # Accept input n as integer only using try-except.
    try:
        n = int(input("Enter n: "))
    except ValueError:
        print("This script accepts only integer value for n. Exiting script!")
        sys.exit(1)
    n = abs(n)  # Converting n to positive value if negative value given.
    our_sum = calculate_sum(n)  # Call function to calculate sum.
    print(f"\nThe sum of first {n} numbers is: {our_sum}\n")
    return None

# Call main function if this script is executed.
if __name__ == "__main__":
    main()
