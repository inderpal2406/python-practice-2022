"""Module to find sum & average of digits present in a string"""

# Import modules.

import clear_screen_module

# Define functions.

def sum_avg_of_digits_in_str(fnstr):
    """Function to find sum & average of digits in a string"""
    oursum = 0
    numlist = []
    for eachchar in fnstr:
        #print(eachchar,type(eachchar))
        if ord(eachchar) in list(range(48,58,1)):
            intnum = int(eachchar)
            oursum = oursum + intnum
            numlist.append(intnum)
    avg = oursum/len(numlist)
    average = round(avg,2)
    print(f"String: {fnstr}")
    print(f"Digits present in the string are: {numlist}")
    print(f"Sum of digits in the string is: {oursum}")
    print(f"Average of digits in the string is: {average}\n")

def main():
    """First function to be called"""
    clear_screen_module.clear_screen()
    print("This script calculates sum & average of digits present in a string.")
    print("Press ENTER to proceed.")
    input()
    str1 = "PYnative29@#8496"
    sum_avg_of_digits_in_str(str1)
    str2 = "Hello$37H3ll0"
    sum_avg_of_digits_in_str(str2)

# Call main() when the script is executed.

if __name__ == "__main__":
    main()
