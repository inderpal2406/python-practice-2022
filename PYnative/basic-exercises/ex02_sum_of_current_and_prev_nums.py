"""Module to calculate sum of current and previous numbers for first 10 numbers"""

# Import modules.

import time
import clear_screen_module

# Define functions.

def SumOfCurrentAndPrevious():
    """Function to calculate & display sum of current number & previous number"""
    """For first 10 numbers"""
    for num in range(1,11,1):
        prev_num = num - 1
        addsum = num + prev_num
        print(f"Current number: {num} Previous number: {prev_num} Sum: {addsum}")
        time.sleep(1)

def main():
    """First function to be called"""
    clear_screen_module.clear_screen()
    print('''
    This script displays sum of current & previous numbers,
    for first 10 numbers. Press ENTER to proceed.
    ''')
    input() # Read ENTER key.
    SumOfCurrentAndPrevious()
    print() # Leave a line a end.

# Call main() when the script is executed.

if __name__ == "__main__":
    main()
