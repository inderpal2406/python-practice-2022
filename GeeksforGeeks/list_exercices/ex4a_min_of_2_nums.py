"""Module to find smallest of 2 numbers"""

# Import modules.

import sys
import clear_screen_module

# Define functions.

def main():
    """First function to be called"""
    clear_screen_module.clear_screen()
    print("This script will accept 2 nums & display smallest of the two.\n")
    try:
        num1 = eval(input("Enter first number: "))
        num2 = eval(input("Enter second number: "))
    except Exception:
        print("Please enter a number only. Exiting script!")
        sys.exit(1)
    # eval() allows input as bool value as well.
    # Check if bool value is supplied. If yes, then exit.
    if (type(num1) is bool or type(num2) is bool):
        print("Please enter a number only. Exiting script!")
        sys.exit(1)
    numlist = []
    numlist.append(num1)
    numlist.append(num2)
    numlist.sort()
    #print(numlist)
    print(f"The minimum number amongst {num1} & {num2} is: {numlist[0]}\n")
    return None

# Call main() if the script is executed.

if __name__ == "__main__":
    main()
