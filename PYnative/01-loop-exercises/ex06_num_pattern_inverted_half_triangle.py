"""Module to print number pattern in form of an inverted half triangle"""

# Import modules.

import clear_screen_module

# Define functions.

def PrintInvertedHalfTriangle(fnnum):
    """Funtion to print inverted half triangle pattern of numbers"""
    for eachnum in range(fnnum,0,-1):
        while eachnum >= 1:
            print(eachnum,end="")
            eachnum = eachnum - 1
        print() # Bring cursor to new line.

def main():
    """First function to be called"""
    clear_screen_module.clear_screen()
    print('''
    This script prints a number pattern in form of inverted half triangle.
    Press ENTER to proceed.
    ''')
    input()
    num = 5
    print("The pattern is as below,\n")
    PrintInvertedHalfTriangle(num)
    print()

# Call main() when the script is executed.

if __name__ == "__main__":
    main()
