# This script defines a custom module to check if the user input is a boolean value.
# If input is a boolean value then the script will exit the program without further executing the code.
# This can be used where input is not needed as a boolean value.
# Corresponding message is also displayed.

def check_input(value):
    if type(value) is bool:
        print(f"The provided the input {value} is a boolean value, which is not expected. Hence, exiting script now!")
        exit(1)
