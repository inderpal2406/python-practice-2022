# This script will accept sequesnce of comma separated numbers from user and generate a list and tuple from it.
# Important note: When we split a string using the split function, it gives the result as a list of strings. 
# These strings are formed based on the delimiter that we provide as an argument to the split function.
# A list can be converted to a tuple using the tuple() function. Maybe this is called typecasting.
# If we don't specify an input and simple press ENTER, then it creates a list with 1 member but a tuple with 2 members. Need to check why.

# Import modules.

import platform
import os

# Detect the OS and clear the screen.

os_name = platform.system()
if os_name == "Windows":
    os.system("cls")
elif os_name == "Linux":
    os.system("clear")

# Display the purpose of the script.

print(f"This script will accept a sequence of comma separated numbers and generate a list and tuple from it.\n")

# Accept the user input.

user_input = input("Enter the sequence of comma separated numbers: ")

# Convert the user input string to list.

our_list = user_input.split(",")

# Convert the list to tuple.

our_tuple = tuple(our_list)

# Display the output.

print(f"\nList: {our_list}")
print(f"Tuple: {our_tuple}\n")
