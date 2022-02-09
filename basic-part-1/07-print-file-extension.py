# This script will accept a filename from the user and print the extension of that.
# If the script doesn't find a period in filename, then it'll display result accordingly.
# "not in" or "in" membership operator can be used with strings as well along with list, tuples.
# Need to check which additional other places can it be used.

# Import modules.

import platform
import os

# Detect the OS and clear the screen.

os_name = platform.system()
if os_name == "Windows":
    os.system("cls")
elif os_name == "Linux":
    os.system("clear")

# Display purpose of the script.

print(f"This script will accept filename from the user and print its extension.\n")

# Accept user input.

filename = input("Enter the filename: ")

# Check if the filename has a period "." in it. If it contains a period, then extract the extension and display it.

if "." not in filename:
    print(f"\nThe filename doesn't contain . in it. It seems to be a file without extension.\n")
else:
    our_list = filename.split(".")
    print(f"\nFile extension: {our_list[-1]}\n")
