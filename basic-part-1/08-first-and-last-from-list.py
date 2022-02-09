# This script will display the first and last color from a list of colors.

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

print(f"\nThis script will display first and last colors from a list of colors.\n")

# Display the list of colors.

color_list = ["Red","Green","White","Blue","Black"]
print(f"The list of colors is: {color_list}\n")

# Display the first and last color from the list of colors.

print(f"First color: {color_list[0]}")
print(f"Last color: {color_list[-1]}\n")
