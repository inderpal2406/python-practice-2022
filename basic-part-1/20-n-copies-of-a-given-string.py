# This script will accept a string and a number n from a user.
# It'll then join the string n number of times to produce a new string.
# For example, if string is "python" and number n is 2, then new string produced would be "pythonpython"
# the script would fail, if a string value is provided for number n. This would be enhanced later to fail the script gracefully in such a case.

# Import modules.

import clear_screen_module

# Clear the screen.

clear_screen_module.clear_screen()

# Display the purpose of the script.

print(f"This script will accept a string and a number n from a user.")
print(f"It'll then join the string n number of times to produce a new string.")
print(f"For example, if string is \"python\" and number n is 2, then new string produced would be \"pythonpython\"\n")

# Accept the string from the user.

user_string = input("Enter the string: ")

# Accept the number n from the user.

n = eval(input("Enter the number n: "))

if type(n) is int:
    new_string = ""
    i = n
    while i != 0:
        new_string = user_string+new_string
        i = i-1
    print(f"\nThe new string produced from joining your string {n} number of times is as below,")
    print(f"{new_string}\n")
else:
    print(f"\nThe script expects only an int value for n. But you have entered a {type(n)} value for n. Exiting script now!\n")
    exit(1)
