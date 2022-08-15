"""Module to create variable length arguments function"""

# Import modules.

import time
import clear_screen_module

# Define functions.

def CalculateAverage(*nums):
    """Function to calculate average of arguments supplied"""
    #print(f"{type(nums)}") # nums is a tuple
    numofargs = len(nums)
    fn_sum = 0
    for eacharg in nums:
        fn_sum = fn_sum + eacharg
    fn_avg = fn_sum / numofargs
    print(f"Numbers: {nums}")
    print(f"Average: {fn_avg}\n")

def main():
    """First function to be called"""
    clear_screen_module.clear_screen()
    print("""
    This script creates a function to accept variable length arguments,
    and calculate average of arguments supplied, when function is called multiple times,
    with variable length of arguments. Press ENTER to proceed.
    """)
    input()
    CalculateAverage(10,20,30)
    time.sleep(1)
    CalculateAverage(40,50)

# Call main() when the script is executed.

if __name__ == "__main__":
    main()
