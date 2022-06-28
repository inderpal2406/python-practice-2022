"""Module to multiply numbers in a list"""

# Import modules.

import sys
import clear_screen_module

# Define functions.

def main():
    """First function to be called"""
    clear_screen_module.clear_screen()
    print("This script would accept integers and then display their product.\n")
    intlist = []
    index = 0
    try:
        count = int(input("How many integers do you want to multiply: "))
        while index < count:
            num = int(input("Enter the integer: "))
            intlist.append(num)
            index = index + 1
    except ValueError:
        print("Please enter an integer only. Exiting script now!")
        sys.exit(1)
    product = 1
    for eachint in intlist:
        product = product*eachint
    print(f"The product of entered integers is: {product}")

# Call main() if the script is executed.

if __name__ == "__main__":
    main()
