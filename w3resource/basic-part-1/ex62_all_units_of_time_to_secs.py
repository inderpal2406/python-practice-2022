"""Convert all units of time to seconds"""

# This script will display all units of time except seconds.
# Then ask user to select one unit in which he wants to give input.
# Then convert user input to seconds.

# Import modules.

import sys
import clear_screen_module

# Define functions.

def convert_year_to_sec(time_year):
    """Function to convert time in year into secs"""
    ans = time_year * 365 * 24 * 60 * 60
    return ans

def convert_month_to_sec(time_month):
    """Function to convert time in months to secs"""
    ans = time_month * 30 * 24 * 60 * 60
    return ans

def convert_week_to_sec(time_week):
    """Function to convert time in week to secs"""
    ans = time_week * 7 * 24 * 60 * 60
    return ans

def convert_day_to_sec(time_day):
    """Function to convert time in day to secs"""
    ans = time_day * 24 * 60 * 60
    return ans

def convert_hr_to_sec(time_hr):
    """Function to convert time in hr to secs"""
    ans = time_hr * 60 * 60
    return ans

def convert_min_to_sec(time_min):
    """Function to convert time in mins to secs"""
    ans = time_min * 60
    return ans

def main():
    """First function to be called"""
    # Clear screen using module function.
    clear_screen_module.clear_screen()
    print("This script converts the unit of time of user choice to seconds.\n")
    print('''
    1. Minute
    2. Hour
    3. Day
    4. Week
    5. Month
    6. Year
    ''')
    print("Which unit of time do you want to convert to seconds?")
    user_choice = input("Enter your choice [1|2|..|6]: ")
    # Check if user provided valid choice between 1 to 6.
    if user_choice not in ["1","2","3","4","5","6"]:
        print("Invalid choice. Please enter a number between 1 to 6. Exiting now!")
        sys.exit(1)
    # If valid choice given, then aks for input time.
    # Accept a numeric value only using try-except.
    try:
        user_time = eval(input("Enter the time: "))
    except NameError:
        print("Please enter a numeric value only. Exiting script now!")
        sys.exit(1)
    # Do conversion of time to seconds as per the user choice.
    if user_choice == "1":
        time_sec = convert_min_to_sec(user_time)
        print(f"{user_time} minutes = {time_sec} seconds")
    elif user_choice == "2":
        time_sec = convert_hr_to_sec(user_time)
        print(f"{user_time} hours = {time_sec} seconds")
    elif user_choice == "3":
        time_sec = convert_day_to_sec(user_time)
        print(f"{user_time} days = {time_sec} seconds")
    elif user_choice == "4":
        time_sec = convert_week_to_sec(user_time)
        print(f"{user_time} weeks = {time_sec} seconds")
    elif user_choice == "5":
        time_sec = convert_month_to_sec(user_time)
        print(f"{user_time} months = {time_sec} seconds")
        print("Note: The month in this calculation has 30 days.")
    else:
        time_sec = convert_year_to_sec(user_time)
        print(f"{user_time} years = {time_sec} seconds")
        print("Note: The year in this calculation has 365 days.")
    return None

# Call main function if this script is executed.

if __name__ == "__main__":
    main()
