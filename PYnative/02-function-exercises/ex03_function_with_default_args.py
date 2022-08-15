"""Module to create a function with default arguments"""

# Import modules.

import clear_screen_module

# Define functions.

def showEmployee(fn_name,fn_sal=9000):
    """Function to display employee name & salary"""
    print(f"Name: {fn_name} salary: {fn_sal}")

def main():
    """First function to be called"""
    clear_screen_module.clear_screen()
    print("""
    This script shows employee name & his salary, by using a function,
    which has default arguments defined. Press ENTER to proceed.
    """)
    input()
    showEmployee("Ben",12000)
    showEmployee("Jessa")

# Call main() when the script is called.

if __name__ == "__main__":
    main()
