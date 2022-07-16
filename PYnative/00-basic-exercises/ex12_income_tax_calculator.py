"""Module to calculate income tax"""

# Rules to calculate income tax:
# First 10000, nil tax.
# Next 10000, 10% tax.
# On remaining amount, 20% tax.

# Import modules.

import clear_screen_module

# Define functions.

def caltax(inamt):
    """Function to calculate tax"""
    amt1 = inamt - 10000
    amt2 = amt1 - 10000
    tax1 = (10/100)*10000
    tax2 = (20/100)*amt2
    taxamt = tax1 + tax2
    return taxamt

def main():
    """First function to be called"""
    clear_screen_module.clear_screen()
    print("This script calculates income tax. Press ENTER to proceed.\n")
    input()
    income = 45000
    tax = caltax(income)
    print(f"Income is: ${income}")
    print(f"Tax is: ${tax}\n")

# Call main() when the script is executed.

if __name__ == "__main__":
    main()
