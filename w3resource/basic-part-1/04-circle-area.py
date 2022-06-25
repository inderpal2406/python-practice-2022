# This script will accept the radius of a circle from the user and calculate its area.
# Radius can be an integer as well as float number.
# The script would fail if a string is given as input in radius. This will be enhanced later by exception handling.

# Import modules.

import platform
import os
import math

# Detect the OS and clear the screen.

os_name = platform.system()
if os_name == "Windows":
    os.system("cls")
elif os_name == "Linux":
    os.system("clear")

# Display the purpose of the script.

print(f"This script will calculate area of a circle after taking its radius as an input.\n")

# Accept the radius of the circle from the user.

radius = eval(input("Enter the radius of the circle: "))

# Calculate area of the circle.

area = math.pi*radius**2

# Display the area.

print(f"\nArea of the circle is: {area}\n")
