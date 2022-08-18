"""Module to create a str of first, middle & last chars of each input str"""

# Import modules.

import sys
import clear_screen_module

# Define functions.

def main():
    """First function to be called"""
    clear_screen_module.clear_screen()
    print("""
    This script creates a string of first, middle & last characters of
    each input string. Press ENTER to proceed.\n
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
    charlist = []
    str1mid = str1len // 2
    str2mid = str2len // 2
    charlist.append(str1[0])
    charlist.append(str2[0])
    charlist.append(str1[str1mid])
    charlist.append(str2[str2mid])
    charlist.append(str1[-1])
    charlist.append(str2[-1])
    ansstr = ''.join(charlist)
    print(f"Input string 1: {str1}\nInput string 2: {str2}")
    print(f"Answer string: {ansstr}\n")
    #print(str1,str2,ansstr)

if __name__ == "__main__":
    main()
