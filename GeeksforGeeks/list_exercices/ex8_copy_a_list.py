"""Module to copy/clone a list"""

import clear_screen_module

def main():
    """First function to be called"""
    clear_screen_module.clear_screen()
    print("This script will copy/clone a list.\n")
    alphalist = ["a","b","c","d","e"]
    copylist = alphalist.copy()
    print(f"Given list is: {alphalist}")
    print(f"Cloned list is: {copylist}\n")

if __name__ == "__main__":
    main()
