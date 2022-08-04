"""Module to print prime numbers within a range"""

# Import modules.

import sys
import clear_screen_module

# Define functions.

def CalPrimeWithinRange(fnstartnum,fnendnum):
    """Function to calculate prime nums upto n"""
    #if fnnum_n in [0,1]:
        #print("\n0 & 1 are not considered as prime or composite numbers. Exiting script!\n")
        #sys.exit(1)
    fnprime_num_list = []
    for eachnum in range(fnstartnum,fnendnum+1,1):
        index = 1
        factors = []
        while index <= eachnum:
            if eachnum%index == 0:
                factors.append(index)
            index = index + 1
        if len(factors) == 2:
            fnprime_num_list.append(eachnum)
    return fnprime_num_list

def main():
    """First function to be called"""
    clear_screen_module.clear_screen()
    print("This script prints prime numbers within a range from start num to end num.\n")
    try:
        startnum = int(input("Enter the start number: "))
        endnum = int(input("Enter the end number: "))
    except ValueError:
        print("\nPlease enter an integer value only. Exiting script now!\n")
        sys.exit(1)
    if startnum < 0 or endnum < 0:
        print("\nPlease enter an integer > 0. Exiting script now!\n")
        sys.exit(1)
    prime_num_list = CalPrimeWithinRange(startnum,endnum)
    print(f"\nThe prime numbers between {startnum} and {endnum} are as below,")
    print(prime_num_list,"\n")

if __name__ == "__main__":
    main()
