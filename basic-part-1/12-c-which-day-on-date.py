# This script will accept a date from user. Then display the day on that date.
# This script is not capable to highlight wrong input data. This would be done later.

import platform
import os
import calendar

# Define functions.

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

print(f"The script will accept a date from user and display the day on that date.\n")

# Accept the date from the user.

user_date = input("Enter the date in the format dd/mm/yyyy : ")

# Process the input and extract the date, month and year. Also convert it to interger data from string data.

only_date = int(user_date.split("/")[0])
only_month = int(user_date.split("/")[1])
only_year = int(user_date.split("/")[2])

# Calculate the day on the date.

day = calendar.day_name[calendar.weekday(only_year,only_month,only_date)]

# Display the day.

print(f"\nDay on {user_date} : {day}\n")
