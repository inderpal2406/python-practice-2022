"""Module with function to calculate exponent of a number"""

# Import modules.

import clear_screen_module

# Define functions.

def exponent(fnbase,fnex):
    """Function to calculate the exponent of base"""
    fnans = fnbase**fnex
    return fnans

def readenter():
    """Function to read ENTER key input"""
    print("\nPress ENTER to proceed.\n")
    input()

def main():
    """First function to be called"""
    clear_screen_module.clear_screen()
    print("This script calculates exponent of a number.")
    readenter()
    basenums = [2,5]
    exnums = [5,4]
    indexlim = len(basenums)
    index = 0
    while index < indexlim:
        exans = exponent(basenums[index],exnums[index])
        print(f"base = {basenums[index]}\nexponent = {exnums[index]}")
        print(f"{basenums[index]} raised to the power of {exnums[index]} is = {exans}")
        readenter()
        index = index + 1
    print("That's it for now. Thank you.\n")

# Call main() when the script is executed.

if __name__ == "__main__":
    main()
