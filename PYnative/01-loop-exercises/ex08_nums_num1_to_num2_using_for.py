"""Module to print numbers -10 to -1 using for loop"""

import time
import clear_screen_module

def PrintNumsByIncrement1(fnnum1,fnnum2):
    """Function to print nums from fnnum1 to fnnum2 by incrmenting 1"""
    print("The numbers are: ")
    for eachnum in range(fnnum1,fnnum2+1,1):
        print(eachnum)
        time.sleep(1)
    print()

def main():
    """First function to be called"""
    clear_screen_module.clear_screen()
    num1 = -10
    num2 = -1
    print(f"This script prints numbers from {num1} to {num2} using for loop.")
    print("Press ENTER to proceed.\n")
    input()
    PrintNumsByIncrement1(num1,num2)

if __name__ == "__main__":
    main()
