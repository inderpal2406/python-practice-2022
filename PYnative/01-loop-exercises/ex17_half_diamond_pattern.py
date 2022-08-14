"""Module to print half diamond pattern"""

# Import modules.

import clear_screen_module

# Define functions.

def PrintHalfDiamond(fn_num):
    """Function to print the half diamond pattern"""
    for eachnum in range(1,fn_num+1,1):
        count = 1
        while count <= eachnum:
            print("*",end="")
            count = count + 1
        print() # Bring cursor to next line.
    for eachnum in range(fn_num-1,0,-1):
        count = 1
        while count <= eachnum:
            print("*",end="")
            count = count + 1
        print() # Bring cursor to next line.

def main():
    """First function to be called"""
    clear_screen_module.clear_screen()
    print("This script prints a half diamond pattern of *")
    print("Press ENTER to proceed.")
    input()
    num = 5
    print("The pattern is as below,\n")
    PrintHalfDiamond(num)
    print() # Leave a line after printing the pattern.

# Call main() when the script is executed.

if __name__ == "__main__":
    main()
