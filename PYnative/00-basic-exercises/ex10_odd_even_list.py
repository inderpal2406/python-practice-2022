"""Module to create  list of odd nums from one list and even nums from another"""

# Import modules.

import time
import clear_screen_module

# Define functions.

def oddevenlist(fnlist1,fnlist2):
    """Function to create list containing odd nums from list1 & even from list2"""
    fnanslist = []
    for eachnum in fnlist1:
        if eachnum%2 == 1:
            fnanslist.append(eachnum)
    for eachnum in fnlist2:
        if eachnum%2 == 0:
            fnanslist.append(eachnum)
    return fnanslist

def main():
    """First function to be called"""
    clear_screen_module.clear_screen()
    print('''
    This script creates a new list containing odd numbers
    from one list and even numbers from another list.
    Press ENTER to proceed.
    ''')
    input()
    list1 = [10,20,25,30,35]
    list2 = [40,45,60,75,90]
    anslist = oddevenlist(list1,list2)
    print(f"list1 = {list1}\nlist2 = {list2}")
    time.sleep(2)
    print(f"result list = {anslist}\n")

if __name__ == "__main__":
    main()
