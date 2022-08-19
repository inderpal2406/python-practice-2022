"""Module to count letters, digits & special symbols from a string"""

# Import modules.

import clear_screen_module

# Define functions.

def count_chars_digits_symbols_from_str(fnstr):
    """Function to count chars, digits & symbols from a string"""
    charlist = []
    digitlist = []
    symbollist = []
    for eachchar in fnstr:
        ascii_code = ord(eachchar)
        if ascii_code in list(range(97,123,1)) or ascii_code in list(range(65,91,1)):
            charlist.append(eachchar)
        elif ascii_code in list(range(48,58,1)):
            digitlist.append(eachchar)
        else:
            symbollist.append(eachchar)
    return len(charlist),len(digitlist),len(symbollist) # return values as tuple
    # We can also write return (a,b,c)

def main():
    """First function to be called"""
    clear_screen_module.clear_screen()
    print("This script counts letters, digits & special symbols from a string.")
    print("Press ENTER to proceed.")
    input()
    ourstr = "P@#yn26at^&i5ve"
    # unpack returned tuple of integers
    chars,digits,symbols = count_chars_digits_symbols_from_str(ourstr)
    print(f"Total counts of chars, digits, and symbols in the string: {ourstr}")
    print(f"Chars: {chars}\nDigits: {digits}\nSymbols: {symbols}\n")

if __name__ == "__main__":
    main()
