"""Module to reverse a list"""

import clear_screen_module

def main():
    """First function to be called"""
    clear_screen_module.clear_screen()
    print("This script will reverse a given list.\n")
    mixedlist = [1,2,3,":","&","cat",True,7.8,0.66]
    print(f"Given list is: {mixedlist}")
    mixedlist.reverse()
    print(f"Reversed list is: {mixedlist}\n")

if __name__ == "__main__":
    main()
