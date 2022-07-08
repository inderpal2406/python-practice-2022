"""Module to check if a word has at least 1 letter & 1 number"""

# Import modules.

import sys
import clear_screen_module

# Define functions.

def CalStrNumList():
    """Function to create list of strings of numbers from 0 to 9"""
    fnstrnumlist = []
    for eachnum in range(0,10,1):
        fnstrnumlist.append(str(eachnum))
    return fnstrnumlist

def CalSmallAlphaList():
    """Function to create list of small alphabets"""
    fnsmallalphabetlist = []
    for eachnum in range(97,123,1):
        fnsmallalphabetlist.append(chr(eachnum))
    return fnsmallalphabetlist

def CalCapitalAlphaList():
    """Function to create list of capital alphabets"""
    fncapitalalphabetlist = []
    for eachnum in range(65,91,1):
        fncapitalalphabetlist.append(chr(eachnum))
    return fncapitalalphabetlist

def main():
    """First function to be called"""
    clear_screen_module.clear_screen()
    print("This script checks if the word has atleast one letter & one number.\n")
    userword = input("Enter the word: ")
    wordlist = userword.split()
    if len(wordlist) != 1:
        print("Please enter a single word. Exiting script now!\n")
        sys.exit(1)
    strnumlist = CalStrNumList()
    smallalphabetlist = CalSmallAlphaList()
    capitalalphabetlist = CalCapitalAlphaList()
    numcount = 0
    lettercount = 0
    for eachchar in userword:
        if eachchar in strnumlist:
            numcount = numcount + 1
        if eachchar in smallalphabetlist or eachchar in capitalalphabetlist:
            lettercount = lettercount + 1
    if numcount != 0 and lettercount != 0:
        print(f"Given word <{userword}> has atleast one letter & one number.\n")
    elif numcount == 0 and lettercount == 0:
        print(f"Given word <{userword}> has no letter & no number in it.\n")
    elif numcount == 0:
        print(f"Given word <{userword}> doesn't has any number in it.\n")
    #elif lettercount == 0:
    # simple else will also work in place of above condition due to other
    # conditions being evaluated before this.
    else:
        print(f"Given word <{userword}> doesn't has any letter in it.\n")

if __name__ == "__main__":
    main()
