# This script is an enhancement to previous LCM script.
# This script will calculate LCM of 2 positive integers based on a formula.
# In this way, we would always find an LCM as compared to previous script which tries to find LCM 
# from first 10 multiples only.
# Formula of LCM: |a.b| / gcd(a,b)

# Import modules.

import clear_screen_module
from gcd_of_2_positive_integers import calculate_gcd   # needed to call function to calculate GCD.
# import gcd_of_2_positive_integers
# If we import in above way, then we need to use gcd_of_2_positive_integers.calculate_gcd(num1,num2) syntax.
# import gcd-of-2-positive-integers won't work as we have - in name. Python needs only _ in module names.
# import 31_gcd_of_2_positive_integers won't work as python doesn't need a number at start of module name.

# Define functions.

def calculate_lcm(num1,num2):
    print(f"\nCalculating LCM...")
    # Calculate GCD of num1 and num2.
    gcd = calculate_gcd(num1,num2)
    # Calculate LCM of num1 and num2.
    result = (num1*num2)/gcd
    # Return the LCM (result)
    return int(result)  # Previously, it was returning x.0 as LCM due to division operation. int() would avoid this.

def main():
    # Clear the screen.
    clear_screen_module.clear_screen()
    # Display purpose of the script.
    print(f"This script will accept 2 positive integers and calculate their LCM.\n")
    # Accept the integers from the user and exit script by raising an exception if non-int values are provided.
    try:
        int1 = int(input("Enter the first integer: "))
        int2 = int(input("Enter the second integer: "))
    except ValueError:
        print(f"This script accepts only int values. You have provided a non-int value. Exiting the script now!")
        exit(1)
    # Exit script if negative int is provided as we'll operate only on positive ints.
    if int1 < 0 or int2 < 0:
        print(f"You have provided a negative integer. Please provide only positive integer. Exiting script now!")
        exit(1)
    # Calculate LCM.
    lcm = calculate_lcm(int1,int2)
    # Display LCM.
    print(f"The LCM of {int1} and {int2} is {lcm}.\n")
    return None

# Main code starts here.

if __name__ == "__main__":
    main()
