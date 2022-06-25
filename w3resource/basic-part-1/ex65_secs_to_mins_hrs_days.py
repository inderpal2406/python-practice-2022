"""Module to convert secs to mins, hrs and days"""

# This script will convert seconds to minutes, hours and days.
# User will provide seconds as input.

# Import modules.

import sys
import clear_screen_module

# Define functions.

def convert_secs_to_days(secs_time):
    """Function to convert secs to days"""
    ans = ((secs_time/60)/60)/24
    return round(ans,2) # Round off the ans to 2 decimal points.

def convert_secs_to_hrs(secs_time):
    """Function to convert secs to hrs"""
    ans = (secs_time/60)/60
    return round(ans,2)

def convert_secs_to_mins(secs_time):
    """Function to convert secs to mins"""
    ans = secs_time / 60
    return round(ans,2)

def main():
    """First function to be called"""
    # Clear screen using module function.
    clear_screen_module.clear_screen()
    print("This script converts secs to mins, hrs & days.\n")
    # Accept a numeric value for secs from user using try-except.
    # Exit script if non-numeric value is provided.
    try:
        user_secs = eval(input("Enter the seconds: "))
    except NameError:
        print("The script accepts numeric value only. Exiting script now!")
        sys.exit(1)
    # Call function to convert secs to mins.
    mins_time = convert_secs_to_mins(user_secs)
    print(f"\n{user_secs} seconds of time = {mins_time} minutes")
    # Call function to convert secs to hours.
    hrs_time = convert_secs_to_hrs(user_secs)
    print(f"{user_secs} seconds of time = {hrs_time} hours")
    # Call function to convert secs to days.
    days_time = convert_secs_to_days(user_secs)
    print(f"{user_secs} seconds of time = {days_time} days\n")
    return None

# Call main function if this script is executed.

if __name__ == "__main__":
    main()
