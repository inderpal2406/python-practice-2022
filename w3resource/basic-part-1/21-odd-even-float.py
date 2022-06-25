# This script will accept a number from the user.
# Then the script would check if the number is odd or even and then display the result.
# In addition, the script would also detect if the user entered a float number and would tell the user to enter only an integer in such a case.
# The script would fail if the user provides a string as an input. This could be enhanced later.

# Import modules.

import platform
import os

# Detect the OS type and clear the screen.

os_name=platform.system()
if os_name == "Windows":
    os.system("cls")
elif os_name == "Linux":
    os.system("clear")

# Display purpose of the script.

print(f"This script will check if the entered number is odd or even.\n")

# Accept user input.

num1=eval(input("Enter a number: "))

# Check if the number is odd or even and display result.

remainder=num1%2
if remainder == 0:
    print(f"{num1} is an even number.\n")
elif remainder == 1:
    print(f"{num1} is an odd number.\n")
else:
    # The remainder would be a float number when a float number is divided by 2. Hence, this condition would hold true for float number inputs.
    print(f"{num1} is a float number. Please enter an integer only.\n")
