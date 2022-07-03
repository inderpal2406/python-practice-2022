"""Module to print half diamond star pattern"""

# Import modules.

import sys
import clear_screen_module

# Define functions.

def half_diamond_star(int_N):
    """Function to print half diamond star pattern."""
    for num1 in range(1,int_N+1,1):
        # A for or a while loop can be used for same purpose.
        # A for loop intrduces an extra var num2 not being used. Hence, while loop.
        '''
        for num2 in range(1,num1+1,1):
            print("*", end="")
        print()
        '''
        index = 1
        while index <= num1:
            print("*", end="")
            index = index + 1
        print()
    for num1 in range(int_N-1,0,-1):
        '''
        for num2 in range(1,num1+1,1):
            print("*", end="")
        print()
        '''
        index = 1
        while index <= num1:
            print("*", end="")
            index = index + 1
        print()

def main():
    """First function to be called"""
    clear_screen_module.clear_screen()
    print("This script accepts an integer N & prints half diamond star pattern.\n")
    try:
        userint = int(input("Enter the integer N: "))
    except ValueError:
        print("Please enter an integer value only. Exiting script now!\n")
        sys.exit(1)
    # Print pattern if userint is between 1 to 10.
    if userint == 0:
        print("No pattern for integer 0.\n")
    elif userint < 0:
        print("No pattern for negative integers.\n")
    elif userint > 10:
        print("Pattern for integer > 10 is big. Please enter integer <= 10.\n")
    else:
        print(f"The pattern for {userint} is:\n")
        half_diamond_star(userint)

# Call main() if the script is executed.

if __name__ == "__main__":
    main()
