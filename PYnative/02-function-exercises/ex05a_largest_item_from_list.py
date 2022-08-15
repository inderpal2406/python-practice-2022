"""Module to find largest item from a given list"""

# Import modules.

import clear_screen_module

# Define functions.

def FindLargestInList(fn_numlist):
    """Function to find largest item in the fn_numlist"""
    fn_numlist.sort()   # sort() will sort in ascending order by default.
    fn_largestnum = fn_numlist[-1]
    return fn_largestnum

def main():
    """First function to be called"""
    clear_screen_module.clear_screen()
    print("""
    This script finds the largest number from a given list.
    Press ENTER to proceed.
    """)
    input()
    numlist = [4,6,8,24,12,2]
    print(f"List: {numlist}")
    largestnum = FindLargestInList(numlist)
    # numlist & fn_numlist may point to same address in memory where the list is stored.
    # Sorting one of them sorts the list at the location.
    # And the other variable is automatically sorted.
    # So, we print list before calling function which sorts the list & below statement is commented.
    #print(f"List: {numlist}")
    print(f"The largest item is: {largestnum}\n")

# Call main() when the script is executed.

if __name__ == "__main__":
    main()
