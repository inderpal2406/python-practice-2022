"""Module to check if the entered string is a palindrome/symmetrical string"""

# Import modules.

import clear_screen_module

# Define functions.

def checkpalindrome(textstr):
    """Function to check if string is palindrom/symmetrical or not"""
    strlist = []
    index = 0
    while index < len(textstr):
        strlist.append(textstr[index])
        index = index + 1
    strlist.reverse()
    reversestr = ''.join(strlist)
    #if textstr == reversestr:
    #    return True
    #else:
    #    return False
    # Above if-else construct does the same as below return statement.
    # We are directly testing the condition inside bool()
    # If condition is true, it returns True else False is returned.
    return bool(textstr == reversestr)

def main():
    """First function to be called"""
    clear_screen_module.clear_screen()
    print("This script checks if the provided string is symmetrical or not.\n")
    userstr = input("Enter the string: ")
    if checkpalindrome(userstr):
        print(f"{userstr} is symmetrical or a palindrome string.\n")
    else:
        print(f"{userstr} is not a symmetrical/palindrome string.\n")

# Call main() when the script is executed.

if __name__ == "__main__":
    main()
