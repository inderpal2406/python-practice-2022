"""Module to make later half of a word in upper case"""

# Import modules.

import sys
import clear_screen_module

# Define functions.

def CheckIfSingleWord(ourstr):
    """Function to check if ourstr is a single word or not"""
    strlist = ourstr.split()
    if len(strlist) == 1:
        return True
    else:
        return False

def main():
    """First function to be called"""
    clear_screen_module.clear_screen()
    print("This script makes the later half of the word as Upper Case.\n")
    userword = input("Enter the word: ")
    if CheckIfSingleWord(userword):
        halflen = len(userword)//2
        firsthalf = userword[0:halflen]
        secondhalf = userword[halflen:]
        uppersecondhalf = secondhalf.upper()
        answord = ''.join([firsthalf,uppersecondhalf])
        print(answord)
    else:
        print("Please enter a single word. Exiting script now!\n")
        sys.exit()

# Call main() when the script is executed.

if __name__ == "__main__":
    main()
