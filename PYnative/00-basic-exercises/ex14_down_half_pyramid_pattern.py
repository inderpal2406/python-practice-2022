"""Module to print downward half pyramid star pattern"""

# Import modules.

import clear_screen_module

# Define functions

def PrintDownHalfPattern(fnnum):
    """Function to print the downward half pyramid pattern"""
    for eachnum in range(fnnum,0,-1):
        index = 1
        while index <= eachnum:
            print("*", end="")
            index = index + 1
        print()

def main():
    """First function to be called"""
    clear_screen_module.clear_screen()
    print("This script prints a downward half pyramid * pattern.")
    print("Press ENTER to proceed.\n")
    input()
    num = 5
    print("The pattern is:\n")
    PrintDownHalfPattern(num)
    print() # Leave a line at the end.

# Call main() when the script is executed.

if __name__ == "__main__":
    main()
