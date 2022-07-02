"""Module to reverse the words in a sentence/string"""

import clear_screen_module

# Define functions.

def reversesentence(inputstr):
    """Function to reverse the sentence"""
    strlist = inputstr.split()
    strlist.reverse()
    ansstr = ' '.join(strlist)
    return ansstr

def main():
    """First function to be called"""
    clear_screen_module.clear_screen()
    print("This script reverses words of the provided sentence.\n")
    usrstr = input("Enter the sentence: ")
    reversestr = reversesentence(usrstr)
    print(f"\nThe entered sentence: {usrstr}")
    print(f"The reversed sentence: {reversestr}\n")

# Call main() when the script is executed.

if __name__ == "__main__":
    main()
