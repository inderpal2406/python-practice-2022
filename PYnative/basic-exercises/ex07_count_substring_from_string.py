"""Module to count substring from a string"""

import clear_screen_module

def countsubstr(fnstr,fnsubstr):
    """Function to count fnsubstr in fnstr"""
    wordlist = fnstr.split()
    anscount = wordlist.count(fnsubstr)
    return anscount

def main():
    """First function to be called"""
    clear_screen_module.clear_screen()
    print("This script counts substring from a string.")
    print("Press ENTER to continue.\n")
    input()
    ourstr = "Emma is a good developer. Emma is a writer."
    substr = "Emma"
    count = countsubstr(ourstr,substr)
    print(f"Given string: {ourstr}")
    print(f"Sub-string: {substr}")
    print(f"{substr} appeared {count} times.\n")

if __name__ == "__main__":
    main()
