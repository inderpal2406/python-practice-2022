"""Module to accept list of 5 float numbers from a user"""

# Import modules.

import sys
import clear_screen_module

# Define functions.

def main():
    """First function to be called"""
    clear_screen_module.clear_screen()
    print("This script accepts 5 float numbers & then displays them as a list.")
    print("Press ENTER to proceed.")
    input()
    floatlist = []
    count = 1
    while count <= 5:
        try:
            num = float(input("Enter the float number: "))
        except ValueError:
            print("The script accepts only float numbers. Exiting script now!\n")
            sys.exit(1)
        floatlist.append(num)
        count = count + 1
    print(f"\nThe list of float numbers is: {floatlist}\n")

# Call main() when the script is executed.

if __name__ == "__main__":
    main()
