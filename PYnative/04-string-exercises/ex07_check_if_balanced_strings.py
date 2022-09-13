"""Module to check if 2 strings are balanced"""

# Suppose we have 2 strings. If all chars of first string are present
# in the second string, then we can say that the 2 strings are balanced.

# Import modules.

import time
import clear_screen_module

# Define functions.

def check_if_balanced_strings(fnstr1,fnstr2):
    """Function to check if the strings are balanced"""
    str1len = len(fnstr1)
    str2len = len(fnstr2)
    if str1len < str2len:
        smallstr = fnstr1
        bigstr = fnstr2
    else:
        smallstr = fnstr2
        bigstr = fnstr1
    count = 0
    for eachchar in smallstr:
        if eachchar in bigstr:
            count = count + 1
        else:
            break
    print(f"First string: {fnstr1}\nSecond string: {fnstr2}")
    if count == len(smallstr):
        print("The two strings are balanced.\n")
    else:
        print("The two strings are not balanced.\n")

def main():
    """First function to be called"""
    clear_screen_module.clear_screen()
    print("""
    This script checks if 2 strings are balanced or not.
    If all characters of smaller string are present in other
    string, then we say that the 2 strings are balanced.
    Press ENTER to proceed.
    """)
    input()
    str1 = "Py"
    str2 = "Python"
    str3 = "Hello"
    str4 = "World"
    check_if_balanced_strings(str1,str2)
    time.sleep(1)
    check_if_balanced_strings(str3,str4)

# Call main() when the script is executed.

if __name__ == "__main__":
    main()
