# This script will ask user to provide a year. Then check if the year is a leap year or not.
# The script will fail if user provides string as an input.

# Import modules.

import platform
import os
import calendar

# Define functions.

def valid_input(user_input):
    if type(user_input) is float:
        print(f"You entered a float number as the year, which is invalid. Please enter a valid year number. Exiting script now!")
        exit(1)
    elif type(user_input) is bool:
        print(f"You entered a boolean value as the year, which is invalid. Please enter a valid year number. Exiting script now!")
        exit(1)
    elif type(user_input) is int:
        if user_input <= 0:
            print(f"You have entered an invalid number as year. Please provide correct year number. Exiting script now!")
            exit(1)
    else:
        print(f"An unrecognized data input type is provided, which the script cannot process. Hence, exiting script now!")
        exit(1)

# Function to clear the screen as per the OS type.
def clear_screen():
    os_name = platform.system()
    if os_name == "Windows":
        os.system("cls")
    elif os_name == "Linux":
        os.system("clear")

# Clear the screen.

clear_screen()

# Display purpose of the script.

print(f"This script will check if the user provided year is a leap year of not.\n")

# Accept year from the user.

user_year = eval(input("Enter the year (Example: 2022): "))

# Check if the user provided year is a valid year or not.

valid_input(user_year)

# Check if the user provied year is a leap year or not and display result.

if calendar.isleap(user_year):
    print(f"\nThe year {user_year} is a leap year.")
else:
    print(f"\nThe year {user_year} is not a leap year.")
