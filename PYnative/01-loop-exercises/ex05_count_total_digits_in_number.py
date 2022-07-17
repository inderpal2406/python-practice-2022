"""Module to calculate total number of digits in a number"""

# Import modules.

import clear_screen_module

# Define functions.

def countdigits(fnnum):
    """Function to calculate total number of digits in a number"""
    strnum = str(fnnum)
    return len(strnum)

def main():
    """First function to be called"""
    clear_screen_module.clear_screen()
    print("This script prints total number of digits in a number.")
    print("Press ENTER to proceed.\n")
    input()
    num = 75869
    digitcount = countdigits(num)
    print(f"Number is: {num}")
    print(f"Number of digits in {num}: {digitcount}\n")

# Call main() when the script is executed.

if __name__ == "__main__":
    main()
