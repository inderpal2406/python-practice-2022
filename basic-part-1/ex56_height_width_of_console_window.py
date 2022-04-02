"""Module to display height & width of console window"""

# This script prints height & width of console window.

# Import modules.

import os
import clear_screen_module

# Define functions.

def main():
    """First function to be called"""
    # Clear screen using module function.
    clear_screen_module.clear_screen()
    print("This script prints console window size in rows & columns.\n")
    print(f"Number of rows: {os.get_terminal_size().lines}")
    print(f"Number of columns: {os.get_terminal_size().columns}\n")
    return None

# Call main() function when this script is executed.

if __name__ == "__main__":
    main()
