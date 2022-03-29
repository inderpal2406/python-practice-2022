"""Convert length in ft to in, yards & miles"""

# This script will convert length in ft to inches, yards & miles.
# Length would be accepted from user.

# Import modules.

import sys
import clear_screen_module

# Define functions.

def convert_ft_to_mi(len_ft):
    """Function to convert length in ft to miles"""
    ans = len_ft * 0.000189
    # round() helps round off the ans to 2 decimal spaces only.
    return round(ans,2)

def convert_ft_to_yd(len_ft):
    """Function to convert length in ft to yards"""
    ans = len_ft * 0.33
    return round(ans,2)

def convert_ft_to_in(len_ft):
    """Function to convert length in ft to inches"""
    ans = len_ft * 12
    return round(ans,2)

def main():
    """First function to be called"""
    # Clear screen using module function.
    clear_screen_module.clear_screen()
    print("This script will convert length in ft to inches, yards & miles.\n")
    # Accept numeric value only for length from user using try-except.
    try:
        user_len = eval(input("Enter the length: "))
    except NameError:
        print("The script accepts only numeric value for length. Exiting script!")
        sys.exit(1)
    len_in = convert_ft_to_in(user_len)
    print(f"\n{user_len} ft of length = {len_in} inches")
    len_yd = convert_ft_to_yd(user_len)
    print(f"{user_len} ft of length = {len_yd} yards")
    len_mi = convert_ft_to_mi(user_len)
    print(f"{user_len} ft of length = {len_mi} miles\n")
    return None

# Call main function when this script is executed.

if __name__ == "__main__":
    main()
