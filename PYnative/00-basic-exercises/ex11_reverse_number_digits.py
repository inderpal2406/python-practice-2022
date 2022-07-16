"""Extract each digit from a number and print in reverse order"""

# Import modules.

import clear_screen_module

# Define functions.

def main():
    """First function to be called"""
    clear_screen_module.clear_screen()
    print("This script extracts each digit from a number & prints in reverse order.")
    print("Press ENTER to proceed.\n")
    input()
    num = 7536
    print(f"The number is: {num}")
    strnum = str(num)
    charlist = []
    for eachchar in strnum:
        charlist.append(eachchar)
    charlist.reverse()
    for eachchar in charlist:
        print(f"{eachchar} ", end="")
    print("\nThat's it for now.\n")

if __name__ == "__main__":
    main()
