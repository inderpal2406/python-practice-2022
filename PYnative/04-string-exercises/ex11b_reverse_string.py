"""Script to accept CLI argument and reverse a string"""

# Import modules.

import sys
#import clear_screen_module

# Define functions.

def reverse_string(fnstr):
    """Function to reverse the string"""
    charlist = []
    for eachchar in fnstr:
        charlist.append(eachchar)
    charlist.reverse()
    fnrevstr = ''.join(charlist)
    return fnrevstr

def main():
    """First function to be called"""
    #clear_screen_module.clear_screen() # Don't clear screen to see previous execution command.
    if len(sys.argv) == 1:
        print("\nThis script reverses the supplied string.")
        print(f"Proper script execution: python {sys.argv[0]} <string_to_be_reversed>")
        print("Exiting script now!\n")
        sys.exit(1)
    elif len(sys.argv) > 2:
        print("\nThis script accepts only one CLI argument. Exiting script now!\n")
        sys.exit(1)
    else:
        ourstr = sys.argv[1]
        revstr = reverse_string(ourstr)
        print(f"\nThe string is: {ourstr}")
        print(f"Reverse of string is: {revstr}\n")

# Call main() when the script is executed.

if __name__ == "__main__":
    main()
