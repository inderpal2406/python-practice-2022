"""Module to calculate hypotenuse of right angled triangle"""

# This script will accept height and base of right angled triange.
# Then calculate its hypotenuse's length.

# Import modules.

import sys
import math
import clear_screen_module

# Define functions.

def calculate_hypo(b,h):
    """Function to calculate hypotenuse"""
    b_sq = b**2
    h_sq = h**2
    ans = math.sqrt(b_sq+h_sq)
    return ans

def main():
    """First function to be called"""
    # Clear screen using module function.
    clear_screen_module.clear_screen()
    print('''
    This script accepts base and height of a right angled triangle,
    and then calculates hypotenuse of it.
    ''')
    # Accept numeric values only for base & height of triangle.
    try:
        base = eval(input("Enter base: "))
        height = eval(input("Enter height: "))
    except NameError:
        print("This script only accepts numeric value. Exiting script!")
        sys.exit(1)
    # Call function to calculate hypotenuse.
    hypo = calculate_hypo(base,height)
    print(f"Hypotenuse: {hypo}")
    return None

# Call main function when this script is executed.

if __name__ == "__main__":
    main()
