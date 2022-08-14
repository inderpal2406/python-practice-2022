"""Module to create variable length arguments function"""

# Import modules.

import time
import clear_screen_module

# Define functions.

def PrintValues(*nums):
    """Function to print arguments supplied"""
    #print(f"{type(nums)}") # nums is a tuple
    print("Printing values:")
    for eacharg in nums:
        print(eacharg)
        time.sleep(1)
    print() # Leave a line at the end.

def main():
    """First function to be called"""
    clear_screen_module.clear_screen()
    print("""
    This script creates a function to accept variable length arguments,
    and display argument values when function is called multiple times,
    with variable length of arguments. Press ENTER to proceed.
    """)
    input()
    PrintValues(10,20,30)
    PrintValues(40,50)

# Call main() when the script is executed.

if __name__ == "__main__":
    main()
