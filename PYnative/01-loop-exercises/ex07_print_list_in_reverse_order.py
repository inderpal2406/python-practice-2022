"""Module to print a list of numbers in reverse order"""

import time
import clear_screen_module

def PrintReverseList(fnnumlist):
    """Function to print list in reverse order"""
    print(f"List: {fnnumlist}")
    print("Printing the list in reverse order:\n")
    time.sleep(2)
    fnnumlist.reverse()
    for eachnum in fnnumlist:
        print(eachnum)
        time.sleep(1)
    print()

def main():
    """First function to be called"""
    clear_screen_module.clear_screen()
    print("This script prints a list of numbers in reverse order.")
    print("Press ENTER to proceed.")
    input()
    numlist = [10,20,30,40,50]
    PrintReverseList(numlist)

if __name__ == "__main__":
    main()
