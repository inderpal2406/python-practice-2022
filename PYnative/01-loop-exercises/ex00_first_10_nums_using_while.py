"""Module to print first 10 natural numbers using while loop"""

# Import modules.

import clear_screen_module

# Define functions.

def printnums(fnnum):
    """Function to print numbers upto fnnum"""
    index = 1
    while index <= fnnum:
        print(index)
        index = index + 1

def main():
    """First function to be called"""
    clear_screen_module.clear_screen()
    print("This script prints first 10 natural numbers. Press ENTER to proceed.\n")
    input()
    num = 10
    print("The numbers are as below,")
    printnums(num)
    print() # leave a line at the end.

# Call main() when the script is executed.

if __name__ == "__main__":
    main()
