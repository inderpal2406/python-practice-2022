"""Module to create a function that returns multiple values"""

# Use comma to return multiple values from a function, in python.

# Import modules.

import clear_screen_module

# Define functions.

def calculation(fn_num1,fn_num2):
    """Function to calculate sum & difference of two numbers"""
    fn_sum = fn_num1 + fn_num2
    fn_difference = fn_num1 - fn_num2
    return fn_sum,fn_difference # Return multiple values separated by commas.

def main():
    """First function to be called"""
    clear_screen_module.clear_screen()
    print("""
    This script calls a function to calculate sum & difference of
    two numbers & return the sum & difference at same time, to depict a
    function that returns multiple values. Press ENTER to proceed.
    """)
    input()
    num1 = 40
    num2 = 10
    """
    # Get result in tuple format and unpack it.
    total,difference = calculation(num1,num2)  # This works.
    print(f"The numbers are {num1},{num2} & the results are below,")
    print(total,difference)
    """
    res = calculation(num1,num2)    # Get result in tuple format.
    #print(f"{type(res)}")   # returns type as class tuple
    print(f"The numbers are {num1},{num2} & the results are below,")
    print(res)

if __name__ == "__main__":
    main()
