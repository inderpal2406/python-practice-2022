"""Module to check if first & last number in a list is same"""

# Import modules.

import time
import clear_screen_module

# Define functions.

def CheckFirstLast(numlist):
    """Function to check if first & last number in list is same"""
    time.sleep(2)
    '''
    if numlist[0] == numlist[-1]:
        return True
    else:
        return False
    '''
    #return numlist[0] == numlist[-1]   # This also works.
    return bool(numlist[0] == numlist[-1])

def main():
    """First function to be called"""
    clear_screen_module.clear_screen()
    print("This script checks if the first & last number in list is same.\n")
    print("Press ENTER key to proceed...")
    input()
    list1 = [1,2,3,4,5]
    list2 = [10,20,30,40,50,10]
    print(f"Given list: {list1}\nThe result is {CheckFirstLast(list1)}\n")
    print(f"Given list: {list2}\nThe result is {CheckFirstLast(list2)}\n")

# Call main() when the script is executed.

if __name__ == "__main__":
    main()
