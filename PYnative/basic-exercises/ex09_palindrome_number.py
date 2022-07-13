"""Module to check palindrome number"""

# Import modules.

import clear_screen_module

# Define functions.

def checknumpalindrome(num):
    """Function to check if num is palindrome"""
    numstr = str(num)
    charlist = []
    for eachchar in numstr:
        charlist.append(eachchar)
    charlist.reverse()
    revnumstr = ''.join(charlist)
    return num == int(revnumstr)

def main():
    """First function to be called"""
    clear_screen_module.clear_screen()
    print("This script checks if the number is a palindrome.")
    print("Press ENTER to proceed.\n")
    input()
    for eachnum in [121,125,1331,564]:
        print(f"Original number: {eachnum}")
        if checknumpalindrome(eachnum):
            print("Yes. Given number is palindrome.\n")
        else:
            print("No. Given number is not palindrome.\n")
        print("\nPress ENTER to proceed.\n")
        input()
    print("That's it for now. Thank you.\n")

# Call main() when the script is executed.

if __name__ == "__main__":
    main()
