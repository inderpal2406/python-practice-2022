"""Module to reverse a atring"""

# Import modules.

import clear_screen_module

# Define functions.

def reverse_string(fnstr):
    """Function to reverse the string"""
    charlist = []
    for eachchar in fnstr:
        charlist.append(eachchar)
    charlist.reverse()
    revstr = ''.join(charlist)
    print(f"The string is: {fnstr}")
    print(f"The reverse string is: {revstr}\n")

def main():
    """First function to be called"""
    clear_screen_module.clear_screen()
    print("This script reverses a string. Press ENTER to continue.")
    input()
    str1 = "Python"
    str2 = "Java"
    str3 = "Powershell"
    reverse_string(str1)
    reverse_string(str2)
    reverse_string(str3)

# Call main() when the script is executed.

if __name__ == "__main__":
    main()
