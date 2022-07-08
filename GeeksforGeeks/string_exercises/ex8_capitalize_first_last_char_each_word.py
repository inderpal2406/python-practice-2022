"""Module to capitalize first & last character of each word in a sentence"""

# Import modules.

import sys
import clear_screen_module

# Define functions.

def FirstLastCharToUpper(oursentence):
    """Function to convert first & last char of each word in sentence to uppercase"""
    wordlist = oursentence.split()
    answordlist = []
    for eachword in wordlist:
        anscharlist = []
        index = 0
        for eachchar in eachword:
            if index == 0 or index == len(eachword)-1:
                eachchar = eachchar.upper()
            anscharlist.append(eachchar)
            index = index + 1
        answord = ''.join(anscharlist)
        answordlist.append(answord)
    anssentence = ' '.join(answordlist)
    return anssentence

def main():
    """First function to be called"""
    clear_screen_module.clear_screen()
    print("This script capitalizes first & last char of each word in sentence.\n")
    sentence = input("Enter the sentence: ")
    wordlist = sentence.split()
    if len(wordlist) == 1 or len(wordlist) == 0:
        print("Please enter a sentence of two or more words. Exiting script now!\n")
        sys.exit(1)
    uppercasesentence = FirstLastCharToUpper(sentence)
    print(f"Answer sentence is: {uppercasesentence}")

if __name__ == "__main__":
    main()
