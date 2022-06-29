"""Module to find odd integers in a list"""

# Import modules.

import clear_screen_module
import custom_list_functions

# Define functions.

def caloddlist(userlist):
    """Function to find odd numbers in a list"""
    anslist = []
    for eachnum in userlist:
        if eachnum%2 == 1:
            anslist.append(eachnum)
    return anslist

def main():
    """First function to be called"""
    clear_screen_module.clear_screen()
    print("This script accepts integers & displays the odd ones in them.\n")
    numlist = custom_list_functions.accept_ints_in_list()
    if bool(numlist):
        oddlist = caloddlist(numlist)
        if bool(oddlist):
            print(f"The odd integers are: {oddlist}\n")
        else:
            print("No odd integers found.\n")
    else:
        print("Odd integers cannot be found if no input is given.\n")

# Call main() when the script is executed.

if __name__ == "__main__":
    main()
