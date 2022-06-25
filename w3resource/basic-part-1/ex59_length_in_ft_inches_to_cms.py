"""Converting length in ft/inches to cms"""

# This script will accept length from user in ft/inches.
# Then convert it to cms.

# Importing modules.

import sys
import clear_screen_module

# Define functions.

def convert_in_to_cm(inch_len):
    """Function to convert length in inches to cm"""
    cm_len = inch_len * 2.54
    return cm_len

def convert_ft_to_cm(ft_len):
    """Function to convert length in ft to cm"""
    cm_len = ft_len * 30.48
    return cm_len

def main():
    """First function to be called"""
    # Clear screen using module function.
    clear_screen_module.clear_screen()
    print("This script will convert length in ft/inches to cms.\n")
    print('''
    Will you provide length in ft or inches?
    1. Foot
    2. Inches
    ''')
    user_choice = input("Press 1 for foot & 2 for inches: ")
    # Exit script using if block, if user enters a value other than 1 or 2.
    #if user_choice != "1" and user_choice != "2": # This also works.
    if user_choice not in ["1","2"]:
        print("Invalid choice. Please enter 1 or 2 only. Exiting script!")
        sys.exit(1)
    # Exit script using try-except, if user enters a string as length.
    try:
        user_len = eval(input("\nEnter the length (Example: 2): "))
    except NameError:
        print("Please enter a numeric value only for length. Exiting script!")
        sys.exit(1)
    if user_choice == "1":
        ans = convert_ft_to_cm(user_len)
        print(f"\n{user_len} ft of length = {ans} cm\n")
    else:
        ans = convert_in_to_cm(user_len)
        print(f"\n{user_len} in of length = {ans} cm\n")
    return None

# Call main function if this script is executed.

if __name__ == "__main__":
    main()
