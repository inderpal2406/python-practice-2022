# This script will accept a string from a user.
# It'll then check if the string begins with "Is" or not.
# If not, then it'll add "Is" in the front.

# Import modules.

import clear_screen_module

# Clear the screen.

clear_screen_module.clear_screen()

# Display purpose of the script.

print(f"The script will check if the entered string starts with \"Is\". If not, then it'll add \"Is\" to the front.")
print(f"This validation is case sensitive.\n")

# Accept the string from the user.

user_string = input("Enter the string: ")

# Check if user_string begins with "Is" or not. If not, then add "Is" in fornt of it.

if user_string[0:2] == "Is":
    print(f"\nThe provided string \"{user_string}\" already begins with \"Is\". Hence, no action here.\n")
else:
    print(f"\nThe provided string \"{user_string}\" does not begin with \"Is\". Hence, adding \"Is\" to its front as below,")
    print(f"Is{user_string}\n")
