"""Module to clear a list"""

import clear_screen_module

def main():
    """First function to be called"""
    clear_screen_module.clear_screen()
    numlist = [1,2,3,4,5]
    print(f"The list is: {numlist}")
    numlist.clear()
    print(f"The list after clearing is: {numlist}\n")

if __name__ == "__main__":
    main()
    