"""Module to print name & age of a person"""

# Import modules.

import clear_screen_module

# Define functions.

def PrintNameAge(fn_name,fn_age):
    """Function to print name & age of a person"""
    print(f"Name: {fn_name}")
    print(f"Age: {fn_age} years\n")

def main():
    """First function to be called"""
    clear_screen_module.clear_screen()
    print("This script prints name & age os a person.")
    print("Press ENTER to proceed.")
    input()
    name = "Vikram Singh"
    age = 40
    PrintNameAge(name,age)

# Call the main() when the script is executed.

if __name__ == "__main__":
    main()
