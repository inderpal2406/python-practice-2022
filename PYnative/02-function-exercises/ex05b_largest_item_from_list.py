"""Module to find largest item from a given list"""

# Import modules.

import clear_screen_module

# Define functions.

def main():
    """First function to be called"""
    clear_screen_module.clear_screen()
    print("""
    This script finds the largest number from a given list.
    Press ENTER to proceed.
    """)
    input()
    numlist = [4,6,8,24,12,2]
    largestnum = max(numlist)
    print(f"List: {numlist}")
    print(f"The largest item is: {largestnum}\n")

# Call main() when the script is executed.

if __name__ == "__main__":
    main()
