"""Module to print a float number with 2 decimal places."""

import clear_screen_module

def main():
    """First function to be called"""
    clear_screen_module.clear_screen()
    print("This script prints a float number with 2 decimal places.")
    print("Press ENTER to proceed.\n")
    input()
    num = 45.23546
    print(f"Float number: {num}")
    print(f"Float number with 2 decimal places: {round(num,2)}\n")
    #print('%.2f' % num)    # This also works.

if __name__ == "__main__":
    main()
