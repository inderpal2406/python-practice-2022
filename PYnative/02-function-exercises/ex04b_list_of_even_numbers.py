"""Module to generate a list of even numbers between num1 to num2"""

# Import modules.

import clear_screen_module

# Define functions.

def main():
    """First function to be called"""
    clear_screen_module.clear_screen()
    num1 = 4
    num2 = 30
    print(f"This script generates a list of even numbers between {num1} & {num2}.")
    print("Press ENTER to proceed.")
    input()
    evenlist = list(range(num1,num2+1,2))
    print(f"Even num list: {evenlist}\n")

# Call main() when the script is executed.

if __name__ == "__main__":
    main()
