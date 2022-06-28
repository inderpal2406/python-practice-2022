"""Module to find even numbers in a list"""

# Import modules.

import clear_screen_module
import custom_list_functions

# Define functions.

def calevenlist(userlist):
    """Function to find even nums in a list"""
    anslist = []
    for eachnum in userlist:
        if eachnum%2 == 0:
            anslist.append(eachnum)
    return anslist

def main():
    """First function to be called"""
    clear_screen_module.clear_screen()
    print("This script accepts integers and displays the even ones.\n")
    numlist = custom_list_functions.accept_ints_in_list()
    if bool(numlist):
        evenlist = calevenlist(numlist)
        if bool(evenlist):
            print(f"The even integers are: {evenlist}\n")
        else:
            print("No even integers found.\n")
    else:
        print("Even integers cannot be found if no input is given.\n")

# Call main() when the script is executed.

if __name__ == "__main__":
    main()
