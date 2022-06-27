"""Module to calculate sum of number digits in a list"""

# If the list is [12,67,43,50,43], then 
# output list would be [3,13,7,5,7]

import sys
import clear_screen_module

# Define functions.

def calsumlist(intlist):
    """Function to calculate sum of digits of each list item & create new list of sums"""
    sumofdigitslist = []
    for eachitem in intlist:
        total = 0
        numstr = str(eachitem)
        eachiter = 0
        while eachiter < len(numstr):
            num = eachitem%10
            total = total+num
            eachitem = eachitem//10
            eachiter = eachiter + 1
        sumofdigitslist.append(total)
    return sumofdigitslist

def main():
    """First function to be called"""
    clear_screen_module.clear_screen()
    print("This script will calculate sum of number digits in a list.")
    print("For example, if list provided is [23,43,67], then output is [5,7,13]\n")
    numlist = []
    index = 0
    try:
        count = int(input("How many numbers need to be stored in list: "))
        while index < count:
            num = int(input("Enter the number: "))
            numlist.append(num)
            index = index + 1
    except ValueError:
        print("Please enter an integer only. Exiting script now!")
        sys.exit(1)
    sumlist = calsumlist(numlist)
    print(f"The provided list is: {numlist}")
    print(f"The sum of digits list is: {sumlist}")

if __name__ == "__main__":
    main()
