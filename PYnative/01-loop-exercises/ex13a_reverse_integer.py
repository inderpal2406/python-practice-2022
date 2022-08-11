"""Module to reverse an integer"""

# Import modules.

import clear_screen_module

# Define functions.

def reversenum(fnintnum):
    """Function to reverse the integer number."""
    fnstrnum = str(fnintnum)
    charlist = []
    for eachchar in fnstrnum:
        charlist.append(eachchar)
    charlist.reverse()
    fnrevstrnum = ''.join(charlist)
    fnrevnum = int(fnrevstrnum)
    return fnrevnum

def main():
    """First function to be called"""
    clear_screen_module.clear_screen()
    print("This script reverses an integer number.")
    print("Press ENTER to proceed.")
    input()
    intnum = 76542
    revnum = reversenum(intnum)
    print(f"Integer number: {intnum}\nReverse integer number: {revnum}\n")

if __name__ == "__main__":
    main()
