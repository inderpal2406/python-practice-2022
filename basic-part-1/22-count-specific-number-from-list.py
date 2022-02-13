# This script will display a predefined list.
# Then it'll ask the user to enter a number from the list.
# Then it'll display the number of times that number exists in the list.
# The script will fail if a string value is provided. This will be enhanced later to fail the script gracefully in such a case.

# Import modules.

import clear_screen_module

# Clear the screen.

clear_screen_module.clear_screen()

# Display the purpose of the script.

print(f"This script will display a predefined list.")
print(f"Then it'll ask the user to enter a number from the list.")
print(f"Then it'll display the number of times that number exists in the list.\n")

# Define and display the list.

our_list = [1,2,3,2,4,5,3,6,7,5,5,9,10]
print(f"The list is: {our_list}")

# Ask the user to enter a number.

num = eval(input("Enter the number: "))

# Check number of occurences of the number in the list.

if num in our_list:
    count = our_list.count(num)
    print(f"\nThe number {num} exists {count} number of times.\n")
else:
    print(f"\nThe number {num} doesn't exist in the script.\n")
