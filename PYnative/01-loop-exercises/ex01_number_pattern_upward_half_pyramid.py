"""Module to print pattern of upward half pyramid of numbers"""

# Import modules.

import clear_screen_module

# Define functions.

def PrintUpwardHalfPyramidOfNums(fnnum):
    """Function to print pattern of upward half pyramid of numbers"""
    for eachnum in range(1,fnnum+1,1):
        index = 1
        while index <= eachnum:
            print(f"{index} ", end="")
            index = index + 1
        print()

def main():
    """First function to be called"""
    clear_screen_module.clear_screen()
    print("This script prints upward half pyramid pattern of numbers.")
    print("Press ENTER to proceed.\n")
    input()
    num = 5
    print("The pattern is as below,")
    PrintUpwardHalfPyramidOfNums(num)
    print() # leave a line at the end.

# Call main() when the script is executed.

if __name__ == "__main__":
    main()
