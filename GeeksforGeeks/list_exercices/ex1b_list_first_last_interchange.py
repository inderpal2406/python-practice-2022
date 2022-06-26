"""Module to interchange first & last item in a list with another logic"""

# Import modules.

import clear_screen_module

# Define functions.

def main():
    """First function to be called"""
    clear_screen_module.clear_screen()
    print("This script will interchange first & last items of a list.\n")
    numlist = [1,2,3,4,5]
    print(f"List before interchange: {numlist}")
    firstitem = numlist[0]
    lastitem = numlist[-1]
    #print(numlist,firstitem,lastitem)
    numlist[0] = lastitem
    numlist[-1] = firstitem
    print(f"List after interchange: {numlist}\n")
    return None

# Call main() if the script is executed.

if __name__ == "__main__":
    main()
