"""Module to count occurrences of all characters within a string"""

# Import modules.

import clear_screen_module

# Define functions.

def count_each_char(fnstr):
    """Function to count each char occurrence in the string supplied as arg"""
    fndict = {}
    for eachchar in fnstr:
        # Convert everything to lower to make our comparison, case insensitive.
        lower_eachchar = eachchar.lower()
        lower_fnstr = fnstr.lower()
        count = lower_fnstr.count(lower_eachchar)
        fndict.update({eachchar:count})
    print(f"The string is: {fnstr}")
    print(f"The cound of occurrences of each char in the string is: {fndict}\n")

def main():
    """First function to be called"""
    clear_screen_module.clear_screen()
    print("This script counts occurrences of each char in a string.")
    print("Press ENTER to proceed.")
    input()
    str1 = "Apple"
    str2 = "Orange"
    str3 = "Banana"
    count_each_char(str1)
    count_each_char(str2)
    count_each_char(str3)

# Call main() when the script is executed.

if __name__ == "__main__":
    main()
