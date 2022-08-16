"""Module to print three strings using a separator"""

import clear_screen_module

def main():
    """First function to be called"""
    clear_screen_module.clear_screen()
    print("This script prints 3 strings using a separator.")
    print("Press ENTER to proceed.")
    input()
    str1 = "Name"
    str2 = "is"
    str3 = "James"
    #print(str1,str2,str3)   # Default separator is space.
    print(str1,str2,str3,sep="**",end="\n\n")   # Default end is \n. To leave 1 more line, \n\n.

if __name__ == "__main__":
    main()
