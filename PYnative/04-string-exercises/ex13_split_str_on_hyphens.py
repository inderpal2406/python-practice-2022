"""Module to split the string on hyphens"""

# Import modules.

import clear_screen_module

# Define functions.

def split_str_on_hyphens(fnstr):
    """Function to split the str on hyphens"""
    print(f"The string is: {fnstr}")
    strlist = fnstr.split(sep="-")
    print("After spliting the string on hyphens, below substrs got generated,")
    for eachstr in strlist:
        print(eachstr)
    print() # Leave a line at the end.

def main():
    """First function to be called"""
    clear_screen_module.clear_screen()
    print("This script splits the string on hyphens.")
    print("Press ENTER to proceed.")
    input()
    str1 = "Emma-is-a-data-scientist"
    split_str_on_hyphens(str1)

# Call main() when the script is executed.

if __name__ == "__main__":
    main()
