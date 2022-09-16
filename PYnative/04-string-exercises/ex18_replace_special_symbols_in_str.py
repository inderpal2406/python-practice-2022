"""Module to replace each special symbol in the string with #"""

import string
import clear_screen_module

def main():
    """First function to be called"""
    clear_screen_module.clear_screen()
    print("This script replaces each special symbol with # in a string.")
    print("Press ENTER to proceed.")
    input()
    str1 = "/*Jon is @developer & musician!!"
    print(f"The original string: {str1}")
    for eachsymbol in string.punctuation:
        str1 = str1.replace(eachsymbol,"#")
    print(f"String after replacement of special symbols: {str1}\n")

if __name__ == "__main__":
    main()
