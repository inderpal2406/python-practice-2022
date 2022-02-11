# This script will get the difference between a given number and 17.
# If the given number is greater than 17, then double of the difference is returned as answer.

# Import modules.

import clear_screen_module

# Clear the screen.

clear_screen_module.clear_screen()

# Display purpose of the script.

print(f"This script will accept a number and display its difference with 17.")
print(f"If the provided number is greater than 17, then double the difference would be returned.\n")

# Accept the number from the user.

num = eval(input("Enter the number: "))

# Calculate the difference between the number and 17.

if num > 17:
    double_difference = 2*(num-17)
    print(f"\nAs the number {num} is greater than 17, the double of the difference is {double_difference}.\n")
else:
    difference = num-17
    print(f"\nDifference between 17 and the {num} is {abs(difference)}.\n")
