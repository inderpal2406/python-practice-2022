# This script will accept first and last name of the user.
# Then it'll display it in reverse order with  space between the last and first names.
# This script will also remove the extra spaces around the input names if any. Such spaces are usually provided by user by mistake while entering the input.
# At present the script will reverse the names as "Hello last_name first_name."
# In future we can try to reverse the characters in the string. For example, Inderpal Saini would be displayed as iniaS laprednI.

# Import modules.

import platform
import os

# Detect the OS type and clear the screen.

os_name = platform.system()
if os_name == "Windows":
    os.system("cls")
elif os_name == "Linux":
    os.system("clear")

# Display the purpose of the script.

print(f"This script will accept the first & last name and then display them in reverse order.\n")

# Accept the first and last names from the user.

first_name = input("Enter the first name: ")
last_name = input("Enter the last name: ")

# Process the input names and remove extra space at the ends if any.

first_name = first_name.strip()
last_name = last_name.strip()

# Display first and last names in reverse order.

print(f"\nHello {last_name} {first_name}.\n")
