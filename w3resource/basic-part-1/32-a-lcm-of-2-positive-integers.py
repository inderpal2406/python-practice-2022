# This script will calculate LCM of 2 positive integers.

# Import modules.

import clear_screen_module

# Define functions.

def calculate_lcm(num1,num2):
    print(f"\nCalculating LCM...")
    # Define two different empty lists to hold multiples of num1 and num2.
    num1_multiples = []
    num2_multiples = []
    # Calculate first 10 multiples of num1 and num2.
    for i in list(range(1,11,1)):
        num1_multiples.append(num1*i)
        num2_multiples.append(num2*i)
    # Display the multiples.
    print(f"The first 10 multiples of {num1} are: {num1_multiples}")
    print(f"The first 10 multiples of {num2} are: {num2_multiples}")
    # Define empty list to hold common multiples.
    common_multiples = []
    # Find the common multiples.
    for i in num1_multiples:
        if i in num2_multiples:
            common_multiples.append(i)
    # Check if common multiples were found and accordingly take action.
    if bool(common_multiples):
        # Display common multiples.
        print(f"Common multipls of {num1} and {num2} are: {common_multiples}")
        # Sort the common_multiples list in ascending order.
        common_multiples.sort()
        # Fetch the first element of the sorted list of common multples. This is our LCM.
        result = common_multiples[0]
        # Return the LCM (result).
        return result
    else:
        # Display msg of no common multiples.
        print(f"No common multiples found in first 10 multiples of {num1} and {num2}.")
        print(f"There could be a possibility that the common multple could be found in further multiples.")
        print(f"But this script calculates tries to find LCM in first 10 multiples only.")
        return None

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
