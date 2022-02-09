# This script will accept year and month as input from user and would display its calendar.
# This script will fail if a string is provided as input.

# Import modules.

import platform
import os
import calendar

# Define functions.

def valid_input(user_input,tag,limit1,limit2):
    if type(user_input) is float:
        print(f"You entered a float number as the {tag}, which is invalid. Please enter a valid {tag} number. Exiting script now!")
        exit(1)
    elif type(user_input) is bool:
        print(f"You entered a boolean value as the {tag}, which is invalid. Please enter a valid {tag} number. Exiting script now!")
        exit(1)
    elif type(user_input) is int:
        if user_input < limit1 or user_input > limit2:
            if tag == "year":
                print(f"This script will accept a year between 1000 to 9999 only. Please provide an input accordingly. Exiting script now!")
            elif tag == "month":
                print(f"This script will accept a month number between 1 to 12 only. Please provide an input accordingly. Exiting script now!")
            exit(1)
    else:
        print(f"An unrecognized data input type is provided, which the script cannot process. Hence, exiting script now!")
        exit(1)
 

# Detect the OS type and clear the screen.

os_name = platform.system()
if os_name == "Windows":
    os.system("cls")
elif os_name == "Linux":
    os.system("clear")

# Display purpose of the script.

print(f"This script will accept year and month as input and then display that particular month's calendar.\n")

# Accept the year.

user_year = eval(input("Enter the year between the range 1000 to 9999 (Example: 2022): "))

# Check if the user provided year is a valid year.

valid_input(user_year,"year",1000,9999)

# Accept month of the year.

user_month = eval(input("Enter the month in number, with Jan represented as 1 & Dec as 12 (Example: 1): "))

# Check if the user provided month number is a valid month number.

valid_input(user_month,"month",1,12)

# Detect the month from the month number.

month_name = calendar.month_name[user_month]

# Display calendar of the month.

cal_of_month = calendar.month(user_year,user_month)
print(f"\nThe calendar for the month of {month_name}, {user_year} is:\n")
print(f"{cal_of_month}")

# Other functions in calendar module.
#calendar.prmonth(user_year,user_month)         # Same input as calendar.month()
#calendar.monthcalendar(user_year,user_month)   # This didn't give any output.


