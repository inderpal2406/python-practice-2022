"""Module to print cube of all numbers from 1 to a given number"""

# Import modules.

import time
import clear_screen_module

# Define functions.

def PrintCubesOfNums(fnnum):
    """Function to print cubes of numbers from 1 to fnnum"""
    for eachnum in range(1,fnnum+1,1):
        cube = eachnum**3
        print(f"Current number is: {eachnum} and the cube is {cube}")
        time.sleep(1)
    print() # Leave a line at the end.

def main():
    """First function to be called"""
    clear_screen_module.clear_screen()
    num = 6
    print(f"This script prints cubes of all numbers from 1 to {num}.")
    print("Press ENTER to proceed.")
    input()
    PrintCubesOfNums(num)

# Call main() when the script is executed.

if __name__ == "__main__":
    main()
