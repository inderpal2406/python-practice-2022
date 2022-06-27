"""Module to calculate sum and average of list"""

import sys
import clear_screen_module

# Define functions.

def calsum(numlist,length):
    """Function to calculate sum of list items"""
    total = 0
    for index in range(0,length,1):
        total = total + numlist[index]
    return total

def main():
    """First function to be called"""
    clear_screen_module.clear_screen()
    print("This script will accept integers & calculate their sum & average.\n")
    intlist = []
    index = 0
    try:
        count = int(input("How many numbers do you want to calculate: "))
        while index < count:
            num = int(input("Enter the number: "))
            intlist.append(num)
            index = index+1
    except ValueError:
        print("Please enter an integer value only. Exiting script now!")
        sys.exit(1)
    summation = calsum(intlist,count)
    avg = summation/count
    print(f"The sum of numbers is: {summation}")
    print(f"The average of numbers is: {avg}\n")

if __name__ == "__main__":
    main()
