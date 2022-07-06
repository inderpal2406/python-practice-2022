"""Module to count total characters in a string, excluding the spaces"""

# Import modules.

import clear_screen_module

# Define functions.

def CharCountWithoutSpace(ourstr):
    """Function to calculate no of chars in a string, excluding spaces"""
    strlist = ourstr.split()
    count = 0
    for eachstr in strlist:
        eachlen = len(eachstr)
        count = count + eachlen
    return count

def main():
    """First function to be called"""
    clear_screen_module.clear_screen()
    print("This script counts total chars in a string, excluding the spaces.\n")
    userstr = input("Enter the string: ")
    charcount = CharCountWithoutSpace(userstr)
    if charcount == 0:
        print("You didn't type anything :)\n")
    else:
        print(f"Total number of chars in the string, excluding the spaces: {charcount}\n")

if __name__ == "__main__":
    main()
