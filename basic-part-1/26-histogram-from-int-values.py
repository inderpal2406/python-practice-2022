# This script has a list of integers defined.
# this script will create a histogram from these integer values.

# Import modules.

import clear_screen_module

# Define functions.

def main():
    # Clear the screen.
    clear_screen_module.clear_screen()
    # Define the list of integers.
    int_list = [2,4,7,4,3]
    print(f"The list of integers is: {int_list}")
    print(f"The histogram for integer values in the list is as below,")
    for i in int_list:
        print(f"{i} ",end="")
        for j in list(range(i)):
            print(f"*",end="")
        print()

# Main code starts here.

if __name__ == "__main__":
    main()
