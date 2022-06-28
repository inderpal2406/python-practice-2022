"""Module to define custom list functions"""

# Import modules.

import sys

# Define functions.

# Function to accept integers from user & store them one by
# one in the list.

def accept_ints_in_list():
    """Function to accept integers into a list"""
    intlist = []
    index = 0
    try:
        count = int(input("How many integers will you provide: "))
        while index < count:
            num = int(input("Enter the integer: "))
            intlist.append(num)
            index = index + 1
    except ValueError:
        print("Please provide an integer value only. Exiting script now!")
        sys.exit(1)
    return intlist
