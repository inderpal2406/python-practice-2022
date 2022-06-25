# This script will check if the entered number is between 100 to 1000 or 1000 to 2000.
# The script will fail if a string value is passed. It'll be enhanced later to fail the script in this case gracefully.

# Import modules.

import clear_screen_module
import check_input_if_bool_module

# Clear the screen.

clear_screen_module.clear_screen()

# Display purpose of the script.

print(f"This script will check if the entered number lies between which of the following ranges,\n0 to 100,\n100 to 1000,\n1000 to 2000,\n2000 above.\n")

# Accept the user input.

num = eval(input("Enter the number: "))

# Check if valid input is provided. If boolean value is provided then exit the script using the module.

check_input_if_bool_module.check_input(num)

# Check if num lies in range 0 to 100 or 100 to 1000 or 1000 to 2000 or 2000 and above.

if num > 0 and num < 100:
    print(f"The number {num} lies between 0 to 100.\n")
elif num > 100 and num < 1000:
    print(f"The number {num} lies between 100 to 1000.\n")
elif num > 1000 and num < 2000:
    print(f"The number {num} lies between 1000 to 2000.\n")
elif num > 2000:
    print(f"The number {num} lies beyond 2000.\n")
elif any([num == 0, num == 100, num == 1000, num == 2000]):
    print(f"The number {num} is an edge number in the comparison ranges.\n")
else:
    print(f"The number {num} is a negative number which is not defined to be checked in the script.\n")
