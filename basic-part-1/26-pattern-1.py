# This script will accept an integer from the user and print a pattern of * based on the integer value.

# Import modules.

import clear_screen_module

# Define functions.

def print_pattern(num):
    print(f"The pattern is as below for the integer number {num}:")
    # We take upper limit in range function as num+1 because range would generate nums till one less than upper limit.
    for i in list(range(1,num+1,1)):    
        for j in list(range(1,i+1,1)):
            print(f"*",end="")
        print() # To bring cursor to new line after printing * in one line.
    return None

def main():
    # Clear the screen.
    clear_screen_module.clear_screen()
    # Accept the integer number from the user and raise exception if integer number is not provided and exit the script in such a case.
    try:
        user_int = int(input("Enter the integer number: "))
    except ValueError:
        print(f"The script accepts only an integer number as input. You didn't provide an integer number. Exiting script now!")
        exit(1)
    # Print the pattern.
    print_pattern(user_int)
    return None

# Main code starts here.

if __name__ == "__main__":
    main()
