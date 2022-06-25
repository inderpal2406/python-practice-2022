# This is modification of 31-gcd-of-2-positive-numbers.py to work as a module, so that the 
# function calculate_gcd(num1,num2) can be called in other scripts to calculate gcd.

# Import modules.

import clear_screen_module

# Define functions.

def calculate_gcd(num1,num2):
    #print(f"\nCalculating GCD...")
    # Define an empty list to hold divisors of num1.
    num1_divisors = []
    for i in list(range(1,num1+1,1)):
        if num1%i == 0:
            num1_divisors.append(i)
    #print(f"Divisors of {num1} are: {num1_divisors}")
    # Define an empty list to hold divisors of num1.
    num2_divisors = []
    for i in list(range(1,num2+1,1)):
        if num2%i == 0:
            num2_divisors.append(i)
    #print(f"The divisors of {num2} are: {num2_divisors}")
    # Define an empty list to hold common divisors.
    common_divisors = []
    for i in num1_divisors:
        if i in num2_divisors:
            common_divisors.append(i)
    #print(f"The common divisors are: {common_divisors}")
    # Sort the common_divisors list and bring the greatest divisor at the end of the list.
    common_divisors.sort()
    # Store the last element of common_divisors list into result. This is the GCD.
    result = common_divisors[-1]
    # Return the result (GCD).
    return result

def main():
    # Clear the screen.
    clear_screen_module.clear_screen()
    # Display the function of the script.
    print(f"This script will accept 2 positive integers and display their GCD.\n")
    # Accept the 2 integers from the user. Exit script by raising an exception if non-int values are provided.
    try:
        int1 = int(input("Enter the first integer: "))
        int2 = int(input("Enter the second integer: "))
    except ValueError:
        print(f"The script only accepts int values. You have provided non-int value. Exiting script now!")
        exit(1)
    # Check if negative int is not provided. If yes, then exit script by displaying a msg.
    if int1 < 0 or int2 < 0:
        print(f"You have provided a negative int. Please enter a positive int only. Exiting script now!")
        exit(1)
    # Calculate GCD.
    gcd = calculate_gcd(int1,int2)
    # Display GCD.
    print(f"The GCD of {int1} and {int2} is {gcd}.\n")
    return None

# Main code starts here.

if __name__ == "__main__":
    main()
