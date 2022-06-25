# This script will accept 2 numbers.
# Then it'll return "True" if those nums are equal or their sum or different is 5.

# Import modules.

import clear_screen_module

# Define functions.

def main():
    # Clear the screen.
    clear_screen_module.clear_screen()
    # Display purpose of the script.
    print(f"This script will accept 2 numbers. Then it'll return \"True\" if the 2 numbers are equal or their sum or difference is 5.\n")
    # Accept the numbers and exit the script if a non-numeric value is provided.
    try:
        num1 = eval(input("Enter the first number: "))      # eval() can accept string in "". So, need to use another way in future.
        num2 = eval(input("Enter the second number: "))
    except NameError:
        print(f"You have entered a non-numeric value. Please enter a number only. Exiting script now!")
        exit(1)
    except SyntaxError:
        print(f"You have entered a non-numeric value. Please enter a number only. Exiting script now!")
        exit(1)
    except Exception as e:
        print(e)
        exit(1)
    # eval() can accept bool value. If bool value is provided then exit the script.
    if type(num1) is bool or type(num2) is bool:
        print(f"You have provided a boolean value. Script accepts only numeric value. Exiting script now!")
        exit(1)
    if num1 == num2 or num1+num2 == 5 or num1-num2 == 5:
        print(f"The numbers {num1} and {num2} satisfy any one of the below 3 conditions:")
        print(f"1. The numbers are equal.\n2. Their sum is 5.\n3. Their difference is 5.")
    else:
        print(f"The numbers {num1} and {num2} doesn't satisfy any one of the below 3 conditions:")
        print(f"1. The numbers are equal.\n2. Their sum is 5.\n3. Their difference is 5.")

# Main code starts here.

if __name__ == "__main__":
    main()
