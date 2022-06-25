# This script will accept a string and an integer n from the user.
# Then it'll check length of the string.
# If length is less than 2, then display the string formed by joining the whole string n times.
# If length is greater than or equal to 2, then take first 2 characters and join them n times.
# Then display this new string formed.

# Import modules.

import clear_screen_module

# Define functions.

def concatenate_string(num,cat_string):
    # Define empty list to be passed as input to join function in the end.
    element_list = []
    for i in list(range(num)):
        # Fill the empty list with string to be repeated.
        # This will happen n number of times as that many times we want to repeat our string.
        element_list.append(cat_string)
    empty_string = ""   # to be inserted between elements of the list to get final string with repetetive strings.
    result_string = empty_string.join(element_list)
    print(f"\nThe string formed by repeating \"{cat_string}\", {num} number of times is as below,")
    print(result_string,"\n")
    return None

# Clear the screen.

clear_screen_module.clear_screen()

# Display purpose of the string.

print(f"This script will take first two characters of a user entered string and display the string formed by repeating these two characters n number of times.\n")

# Accept string from the user.

user_string = input("Enter the string: ")

# Accept the integer n from the user.

num_n = int(input("Enter the number n: "))

# Check length of the user entered string.

string_length = len(user_string)

# Process the inputs and display results.

if string_length < 2:
    data_string = user_string
    print(f"\nAs the string length is less than 2, the complete string \"{data_string}\" would be taken to operate on...")
    concatenate_string(num_n,data_string)
else:
    data_string = user_string[0:2]
    print(f"\nTaking first two characters \"{data_string}\" to operate on...")
    concatenate_string(num_n,data_string)
