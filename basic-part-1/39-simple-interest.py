# This script will accept the principal amount, time period and rate of interest.
# Then calculate the simple interest (SI)
# then display the total amount which will be received after adding SI.

# Import modules.

import clear_screen_module

# Define functions.

def calculate_si(p,n,r):
    # Calculate SI.
    si = (p*n*r)/100
    result = p+si
    return result

def main():
    # Clear the screen.
    clear_screen_module.clear_screen()
    # Display the purpose of the script.
    print(f"This script will accept principal amount, time period, and rate of interest.")
    print(f"Then calculate the simple interest and display the final amount to be received.\n")
    # Accept the inputs and exit script if non-numeric values are provided by raising exception.
    try:
        principal = float(input("Enter the principal amount: "))
        # Ask if time period is in months or years and accordingly accept the input.
        choice = input("Is time period in months or years? type [m|y]: ")
        if choice.casefold() == "m":
            time = float(input("Enter the number of months: "))
            time = time/12
        elif choice.casefold() == "y":
            time = float(input("Enter the number of years: "))
        else:
            print(f"Invalid choice provided. Please enter [m|y] only. Exiting script now!")
            exit(1)
        roi = float(input("Enter the rate of interest: "))
    except ValueError:
        print(f"Invalid non-numeric data is provided. Please provide only numeric data. Exiting script now!")
        exit(1)
    totalamt = calculate_si(principal,time,roi)
    print(f"The total amount to be received is: {totalamt}")
    return None

# Main code starts here.

if __name__ == "__main__":
    main()
