"""Module to find last position of a substring in a given string"""

# Import modules.

import clear_screen_module

# Define functions:

def main():
    """First function to be called"""
    clear_screen_module.clear_screen()
    print("This script finds last position of a substring in a given string.")
    print("Press ENTER to proceed.")
    input()
    str1 = "Emma is a data scientist who knows Python. Emma works at Google."
    substr1 = "Emma"
    ansindex = str1.rfind(substr1)
    print(f"The string: {str1}\nThe substring: {substr1}")
    print(f"Last occurrence of {substr1} starts at index {ansindex}.\n")

# Call main() when the script is executed.

if __name__ == "__main__":
    main()
