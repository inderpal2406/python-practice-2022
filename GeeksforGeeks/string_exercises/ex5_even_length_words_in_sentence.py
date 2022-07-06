"""Module to find even length words in a string"""

# Import modules.

import clear_screen_module

# Define functions.

def FindEvenLenWords(ourstr):
    """Function to find even length words in a list"""
    wordlist = ourstr.split()
    anslist = []
    for eachword in wordlist:
        if len(eachword)%2 == 0:
            anslist.append(eachword)
    return anslist

def main():
    """First function to be called"""
    clear_screen_module.clear_screen()
    print("This script finds even length words in a sentence.\n")
    userstr = input("Enter the sentence: ")
    EvenLenWordsList = FindEvenLenWords(userstr)
    if len(EvenLenWordsList) == 0:
        print("No even length words found.\n")
    else:
        print(f"Even length words are: {EvenLenWordsList}\n")

if __name__ == "__main__":
    main()
