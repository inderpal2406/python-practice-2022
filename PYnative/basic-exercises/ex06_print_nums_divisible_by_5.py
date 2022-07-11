"""Module to print nums divisible by 5 in a list"""

import clear_screen_module

def CheckDivisibilityBy5(ourlist):
    """Function to check if nums in list is divisible by 5"""
    numsdiv5 = []
    for eachnum in ourlist:
        if eachnum%5 == 0:
            numsdiv5.append(eachnum)
    return numsdiv5

def main():
    """First function to be called"""
    clear_screen_module.clear_screen()
    print("This script prints numbers divisible by 5 in a list.")
    print("Press ENTER to proceed.\n")
    input()
    numlist = [10,20,33,46,55]
    anslist = CheckDivisibilityBy5(numlist)
    print(f"Given list: {numlist}")
    print("Divisible by 5")
    for eachnum in anslist:
        print(eachnum)
    print() # Leave a line at end.

if __name__ == "__main__":
    main()
