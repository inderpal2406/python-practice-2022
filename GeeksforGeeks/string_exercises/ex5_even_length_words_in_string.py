"""Module to find even length words in a string"""

# Import modules.

import clear_screen_module

# Define functions.

def FindEvenLenWords(wordlist):
    """Function to find even length words in a list"""
    anslist = []
    for eachstr in wordlist:
        if len(eachstr)%2 == 0:
            anslist.append(eachstr)
    return anslist

def main():
    """First function to be called"""
    clear_screen_module.clear_screen()
    print("This script finds even length words in a string.\n")
    userstr = input("Enter the string: ")
    strlist = userstr.split()
    evenlenstr = FindEvenLenWords(strlist)
    if len(evenlenstr) == 0:
        print("No even length words found.\n")
    else:
        print(f"Even length words are: {evenlenstr}\n")

if __name__ == "__main__":
    main()
