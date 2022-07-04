"""Module to print an inverted star pattern"""

# Import modules.

import sys
import clear_screen_module

# Define functions.

def inverted_star(int_n):
    """Function to print inverted star pattern for integer int_n"""
    for num in range(int_n,0,-1):
        spacelimit = int_n - num
        index = 1
        while index <= spacelimit:
            print(" ", end="")
            index = index + 1
        index = 1
        while index <= num:
            print("*", end="")
            index = index + 1
        print()

def main():
    """First function to be called"""
    clear_screen_module.clear_screen()
    print("This script accepts integer N & prints pattern of inverted star for N.\n")
    try:
        N = int(input("Enter integer N: "))
    except ValueError:
        print("Please enter integer value only. Exiting script now!\n")
        sys.exit(1)
    # Print inverted star pattern for integer value from 1 to 10 only.
    if N == 0:
        print("No pattern for integer 0.\n")
    elif N < 0:
        print("No pattern for negative integers.\n")
    elif N > 10:
        print("Pattern for N > 10 is too big to fit the screen. So, not printing.\n")
    else:
        print(f"Pattern for N = {N} is:\n")
        inverted_star(N)

# Call main() when the script is executed.

if __name__ == "__main__":
    main()
