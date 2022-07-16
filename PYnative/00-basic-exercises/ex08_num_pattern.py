"""Module to print a pattern of numbers"""

# Import modules.

import clear_screen_module

# Define functions.

def printpattern2(num):
    """Function to print number pattern 2"""
    for eachnum in range(1,num+1,1):
        index = 1
        while index <= eachnum:
            print(eachnum, end="")
            index = index + 1
        print()

def printpattern1(num):
    """Function to print number pattern 1"""
    for eachnum in range(1,num+1,1):
        index = 1
        while index <= eachnum:
            print(index, end="")
            index = index + 1
        print() # Bring cursor to next line.

def readenter():
    """Function to read ENTER key"""
    print("\nPress ENTER key to proceed.\n")
    input()

def main():
    """First function to be called"""
    clear_screen_module.clear_screen()
    print("This script prints 2 number patterns.")
    readenter()
    print("The first pattern is:")
    printpattern1(5)
    readenter()
    print("The second pattern is:")
    printpattern2(5)
    readenter()
    print("That's it for now. Thank you.\n")

if __name__ == "__main__":
    main()
