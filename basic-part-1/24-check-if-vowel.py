# This script will check if the letter provided by the user is a vowel or not.
# Also, if user provides more than one letter, then he'll be asked to provide a single letter only.

# Import modules.

import clear_screen_module

# Define functions.

def main():
    # Clear the screen.
    clear_screen_module.clear_screen()
    # Display purpose of the script.
    print(f"This script will accept a letter from the user and check if it a vowel or not.\n")
    # Ask the user to provide a letter.
    user_string = input("Enter the letter: ")
    # Check if no letter/character is provided.
    # If yes, then exit the script by displaying a message.
    if len(user_string) == 0:
        print(f"You have not entered any character. Please provide only one letter. Exiting script now!")
        exit(1)
    # Check if more than one character is provided.
    # If yes, then exit the script by displaying a message.
    elif len(user_string) > 1:
        print(f"You have entered more than one character. Please provide only one letter. Exiting script now!")
        exit(1)
    # As user has provided only one character, check if it is an alphabet or not.
    user_string_ascii = ord(user_string)    # Get ASCII code of the user input character.
    # Check if the single character provided is an alphabet or not.
    # If not then exit the script by displaying a message.
    # This check would be done by getting the ASCII value of the entered character and check if falls in the range 97 to 122 or 65 to 90.
    # 97 to 122 is ASCII code for small case letters.
    # 65 to 90 is ASCII code for upper case letters.
    # In range function below, we take 91 and 123 as upper limits as range function produces values till one number less than upper limit.
    if user_string_ascii not in list(range(65,91,1)) and user_string_ascii not in list(range(97,123,1)):
        print(f"Your input character {user_string} is not an alphabet. Please enter an alphabet only. Exiting script now!")
        exit(1)
    # As we know now that the user has provided a single alphabet, check if it is a vowel.
    vowel_list = ["a","e","i","o","u"]
    if user_string.casefold() in vowel_list:
        print(f"The letter {user_string} is a vowel.")
    else:
        print(f"The letter {user_string} is not a vowel.")

# Main code starts here by calling the main() function.
if __name__ == "__main__":
    main()
