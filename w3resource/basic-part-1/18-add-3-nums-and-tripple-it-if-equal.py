# This script will add 3 given numbers.
# If the numbers are equal, then the script will return 3 times of their sum.
# The script will fail if a string value is provided. This will be enhanced alater to fail the script gracefully in such a case.

# Import modules.

import clear_screen_module          # Custom module.
import check_input_if_bool_module   # Custom module.

# Define functions.

# Function to add 3 numbers.

def add_3_nums(x,y,z):
    sum = x+y+z
    return sum

# Clear the screen.

clear_screen_module.clear_screen()

# Display the purpose of the script.

print(f"This script will calculate sum of the entered 3 numbers.")
print(f"If the entered 3 numbers are equal, then thrice of their sum would be displayed.\n")

# Accept user input.

num1 = eval(input("Enter the first number: "))
num2 = eval(input("Enter the second number: "))
num3 = eval(input("Enter the third number: "))

# Check if any of the entered values is not a boolean. The script will exit in case boolean value is provided.

check_input_if_bool_module.check_input(num1)
check_input_if_bool_module.check_input(num2)
check_input_if_bool_module.check_input(num3)

# Calculate the sum of the three numbers.

sum = add_3_nums(num1,num2,num3)

# Display output as per the different conditions.

if num1 == num2 and num1 == num3:
    sum_three_times = 3*sum
    print(f"\nAs the numbers provided are all equal, three times of their sum is {sum_three_times}.\n")
else:
    print(f"\nSum of {num1}, {num2} and {num3} is {sum}.\n")
