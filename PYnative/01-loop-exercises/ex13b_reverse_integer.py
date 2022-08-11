"""Module to reverse an integer"""

# Import modules.

import clear_screen_module

# Define functions.

def reverseinteger(fnintnum):
    """Function to reverse an integer number"""
    numlist = []
    while fnintnum != 0:
        digit = fnintnum % 10
        numlist.append(digit)
        fnintnum = fnintnum // 10
    #numlist.reverse()  # No need to reverse as already nums are reversed after division.
    #fnrevintnum = ''.join(numlist) # This fails as join expects string values as argument but finds int.
    #print(numlist)
    lenoflist = len(numlist)
    fnrevintnum = 0
    for eachnum in numlist:
        multiplier = 1
        iteration = lenoflist - 1   # Suppose lenoflist=3, then we need 2 multiplications to get 100. So, 3-1.
        while iteration > 0 :
            multiplier = multiplier * 10
            iteration = iteration - 1
        numprod = eachnum * multiplier
        fnrevintnum = fnrevintnum + numprod
        lenoflist = lenoflist - 1   # To move on to next iteration with reduced multiplications.
    return fnrevintnum

def main():
    """First function to be called"""
    clear_screen_module.clear_screen()
    print("This script reverses an integer number.")
    print("Press ENTER to proceed.")
    input()
    intnum = 12345
    revintnum = reverseinteger(intnum)
    print(f"Number: {intnum}")
    print(f"Reverse number: {revintnum}\n")

# Call main() when the script is executed.

if __name__ == "__main__":
    main()
