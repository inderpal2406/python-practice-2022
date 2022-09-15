"""Module to remove all characters, except integers from a string"""

# Import modules.

import clear_screen_module

# Define functions.

def remove_chars_except_ints(fnstr):
    """Function to remove all chars, except integers from a str"""
    fn_intstr_list = []
    for eachchar in fnstr:
        if ord(eachchar) in list(range(48,58,1)):
            fn_intstr_list.append(eachchar)
    fn_intstr = ''.join(fn_intstr_list)
    return fn_intstr

def main():
    """First function to be called"""
    clear_screen_module.clear_screen()
    print("This script removes all chars, except integers from a str.")
    print("Press ENTER to proceed.")
    input()
    str1 = "I am 25 years and 10 months old."
    intstr = remove_chars_except_ints(str1)
    print(f"The string is: {str1}")
    print(f"Output after removing all characters: {intstr}\n")

# Call main() when the script is executed.

if __name__ == "__main__":
    main()
