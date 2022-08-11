"""Module to print list items at odd indexes"""

# Import modules.

import clear_screen_module

# Define functions.

def PrintOddIndexItem(fnnumlist):
    """Function to print items at odd indexes of the list"""
    for eachnum in fnnumlist:
        index = fnnumlist.index(eachnum)
        if index%2 != 0:
            print(eachnum,end=" ")
    print("\n") # Bring cursor to new line in the end & leave one more line in the end.

def main():
    """First function to be called"""
    clear_screen_module.clear_screen()
    print("This script prints list items from odd indexes of the list.")
    print("Press ENTER to proceed.\n")
    input()
    numlist = [10,20,30,40,50,60,70,80,90,100]
    print(f"Our list: {numlist}\n")
    print("List items at odd indexes are as below,")
    PrintOddIndexItem(numlist)

# Call main() when the script is executed.

if __name__ == "__main__":
    main()
