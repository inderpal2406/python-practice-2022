"""Module to create a str of first, middle & last chars of 2 different strings"""

# This script is with another logic as compared to file ex03a.

# Import modules.

import sys
import clear_screen_module

# Define functions.

def main():
    """First function to be called"""
    clear_screen_module.clear_screen()
    print("""
    This script creates a string of first, middle & last characters of
    2 different strings. Press ENTER to proceed.\n
    """)
    input()
    str1 = "America"
    str2 = "Japan"
    str1len = len(str1)
    str2len = len(str2)
    if str1len%2 == 0:
        print(f"""
        String 1: {str1} has even length. Only odd length strings are suitable
        for these operations. Hence, exiting script now!
        """)
        sys.exit(1)
    if str2len%2 == 0:
        print(f"""
        String 2: {str2} has even length. Only odd length strings are suitable
        for these operations. Hence, exiting script now!
        """)
        sys.exit(1)
    str1mid = str1len // 2
    str2mid = str2len // 2
    # Concatenate strings.
    ansstr = str1[0] + str2[0] + str1[str1mid] + str2[str2mid] + str1[-1] + str2[-1]
    print(f"Input string 1: {str1}\nInput string 2: {str2}")
    print(f"Answer string: {ansstr}\n")
    #print(str1,str2,ansstr)

if __name__ == "__main__":
    main()
