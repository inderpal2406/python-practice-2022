# This script will extract data from a tuple and display in a required format.

# Import modules.

import platform
import os

# Detect the OS type and clear the screen.

os_name = platform.system()
if os_name == "Windows":
    os.system("cls")
elif os_name == "Linux":
    os.system("clear")

# Display purpose of the script.

print(f"This script will extract the exam start date from a tuple and display it.\n")

# Define and display the tuple.

our_tuple = (11,12,2014)
print(f"Exam start date in tuple: {our_tuple}\n")

# Display the exam start date from the tuple.

print(f"The examination will start from: {our_tuple[0]}/{our_tuple[1]}/{our_tuple[2]}\n")
