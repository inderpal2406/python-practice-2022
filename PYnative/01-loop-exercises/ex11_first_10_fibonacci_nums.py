"""Module to print first 10 numbers in fibonacci series"""

# Import modules.

import clear_screen_module

# Define functions.

def PrintFibonacciNums(fntotalnums):
    """Function to print fibonacci numbers"""
    fibonaccilist = [0,1]   # First 2 fibonacci numbers are fixed, so rest needs to be calculated.
    iterations = fntotalnums - 2
    iterationindex = 1
    firstindex = 0
    secondindex = 1
    while iterationindex <= iterations:
        oursum = fibonaccilist[firstindex] + fibonaccilist[secondindex]
        fibonaccilist.append(oursum)
        firstindex = firstindex + 1
        secondindex = secondindex + 1
        iterationindex = iterationindex + 1
    print(f"The first {fntotalnums} fibonacci numbers are:")
    print(fibonaccilist,"\n")

def main():
    """First function to be called"""
    clear_screen_module.clear_screen()
    totalnums = 10
    print(f"This script prints first {totalnums} fibonacci numbers.")
    print("Press ENTER to proceed.")
    input()
    PrintFibonacciNums(totalnums)

# Call main() when the script is executed.

if __name__ == "__main__":
    main()
