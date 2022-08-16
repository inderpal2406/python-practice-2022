"""Module to convert decimal number to octal using print function's output formatting"""

import clear_screen_module

def main():
    """First function to be called"""
    clear_screen_module.clear_screen()
    print("""
    This script converts a decimal number to an octal using print function's
    output formatting. Press ENTER to proceed.
    """)
    input()
    num = 8
    print(f"The octal number of decimal number 8 is {oct(num)}.\n")
    # Online solution is below,
    #print('%o' % num)   # This maybe referred as output formatting.

if __name__ == "__main__":
    main()
