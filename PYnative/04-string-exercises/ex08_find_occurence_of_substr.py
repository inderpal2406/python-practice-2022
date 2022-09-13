"""Module to find all occurences of a substring in another given string by ignoring the case"""

# Import modules.

import time
import clear_screen_module

# Define functions.

def check_substr_in_str(fnsubstr,fnstr):
    """Function to count occurences of substr in str"""
    # We cannot loop through eachword in the string.
    # It always loops through each char in the string, by default.
    # So, we create s list of words from the string sentence to get each word.
    strlist = fnstr.split()
    count = 0
    # We strip . from each word in the fnstr and then compare it with substr
    # (all comparison by converting to lower case to make comparison case insensitive)
    for eachword in strlist:
        if eachword.lower().strip(".") == fnsubstr.lower():
            count = count + 1
    print(f"Sentence: {fnstr}")
    print(f"Substring: {fnsubstr}")
    print(f"Total occurences of substring in the sentence: {count}\n")

def main():
    """First function to be called"""
    clear_screen_module.clear_screen()
    print("""
    This script finds occurences of a substring in another string
    by ignoring the case. Press ENTER to proceed.
    """)
    input()
    substr = "USA"
    str1 = "USA is United States of America."
    str2 = "USA cannot be written as usa."
    str3 = "India is my country."
    check_substr_in_str(substr,str1)
    time.sleep(5)
    check_substr_in_str(substr,str2)
    time.sleep(5)
    check_substr_in_str(substr,str3)

# Call main() when the script is executed.

if __name__ == "__main__":
    main()
