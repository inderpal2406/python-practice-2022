"""Module to accept 3 strings in one input()"""

import clear_screen_module

def main():
    """First function to be called"""
    clear_screen_module.clear_screen()
    print("This script accepts 3 employee names using single input().")
    print("Press ENTER to proceed.")
    input()
    names = input("Enter the 3 employee names separated by space: ")
    #print(f"{type(names)}")    # str class
    namelist = names.split()
    count = 1
    for name in namelist:
        print(f"Name{count}: {name}")
        count = count + 1

if __name__ == "__main__":
    main()
