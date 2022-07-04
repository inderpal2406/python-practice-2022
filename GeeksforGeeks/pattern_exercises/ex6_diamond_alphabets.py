"""Module to print diamond star pattern"""

# Import modules.

import sys
import clear_screen_module

# Define functions.

def diamond_star(int_n):
    """Function to print diamond star pattern for integer int_n"""
    for num in range(1,int_n+1,1):
        spacelimit = int_n - num
        index = 1
        while index <= spacelimit:
            print(" ", end="")
            index = index + 1
        index = 1
        while index <= ((2*num)-1):
            print(chr(index+64), end="")
            index = index + 1
        print()
    for num in range(int_n-1,0,-1):
        spacelimit = int_n - num
        index = 1
        while index <= spacelimit:
            print(" ", end="")
            index = index + 1
        index = 1
        while index <= ((2*num)-1):
            print(chr(index+64), end="")
            index = index + 1
        print()

def main():
    """First function to be called"""
    clear_screen_module.clear_screen()
    print("This script accepts an integer N and prints diamond star pattern for it.\n")
    try:
        N = int(input("Enter the integer N: "))
    except ValueError:
        print("Please enter an integer value only. Exiting script now!\n")
        sys.exit(1)
    # Print diamond pattern if N's value is from 1 to 10.
    if N == 0:
        print("No pattern for integer 0.\n")
    elif N < 0:
        print("No pattern for negative integers.\n")
    elif N > 10:
        print("Pattern for N > 10 is too big to fit the screen. So, not printing.\n")
    else:
        print(f"diamond pattern for N = {N} is:\n")
        diamond_star(N)

if __name__ == "__main__":
    main()
