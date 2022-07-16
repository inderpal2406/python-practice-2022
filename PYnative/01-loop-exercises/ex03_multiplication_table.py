"""Module to print multiplication table of a number"""

# Import modules.

import clear_screen_module

# Define functions.

def PrintMultiplicationTable(num):
    """Function to print multiplication table of a number"""
    for eachnum in range(1,11,1):
        product = num * eachnum
        print(product)

def main():
    """First function to be called"""
    clear_screen_module.clear_screen()
    print("This script prints multiplication table of a number.")
    print("Press ENTER to proceed.\n")
    input()
    num = 2
    print(f"The multiplication table of number {num} is as below,")
    PrintMultiplicationTable(num)
    print() # leave line at the end.

# Call main() when the script is executed.

if __name__ == "__main__":
    main()
