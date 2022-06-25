# This script will print a pattern of * in n number of lines.
# The integer n is accepted from the user.

# Import modules.

import clear_screen_module

# Define functions.

def printpattern(n):
    print(f"\nThe pattern in {n} number of lines is as below,\n")
    for i in list(range(n,0,-1)):
        while i != 0:
            print(f"*",end="")
            i = i-1
        print() # to bring the cursor to next line after printing * in one line.
    return None

def main():
    # Clear the screen.
    clear_screen_module.clear_screen()
    # Display the purpose of the script.
    print(f"This script will print a pattern of * in n number of lines.\n")
    # Accept the number n and exit script if non-int value is provided by raising an exception.
    try:
        num = int(input("Enter the number n: "))
    except ValueError:
        print(f"This script accepts only an integer, which you have not provided. Hence, exiting script now!")
        exit(1)
    # Print pattern.
    printpattern(num)
    return None

# Main code starts here.

if __name__ == "__main__":
    main()
