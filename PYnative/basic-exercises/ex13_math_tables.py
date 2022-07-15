"""Module to print multiplication table from 1 to 10"""

# Import modules.

import clear_screen_module

# Define functions.

def printtable(fnnum1,fnnum2):
    """Function to print multiplication tables from num1 to num2"""
    for numl1 in range(fnnum1,fnnum2+1,1):
        for numl2 in range(1,11,1):
            print(f"{numl1*numl2} ", end="")
        print()

def main():
    """First function to be called"""
    clear_screen_module.clear_screen()
    num1 = 1
    num2 = 10
    print(f"This script will print multiplication tables from {num1} to {num2}.")
    print("Press ENTER to proceed.\n")
    input()
    print("The tables are:\n")
    printtable(num1,num2)

# Call main() when the script is executed.

if __name__ == "__main__":
    main()
