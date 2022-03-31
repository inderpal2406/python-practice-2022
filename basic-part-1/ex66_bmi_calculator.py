"""Module to calculate Body Mass Index"""

# This script accepts weight in kg and height in meter from user.
# Then calculates BMI.
# Then displays if person is underweight, normal, overweight or
# obese, based on the BMI.

# Import modules.

import sys
import clear_screen_module

# Define functions.

def classify_bmi(bmi):
    """Function to classify BMI into categories"""
    if bmi <= 18.5:
        return "underweight"
    elif bmi <= 25: # Using elif after return is flagged by pylint. Check it out.
        return "normal"
    elif bmi <= 30:
        return "overweight"
    else:
        return "obese"

def calculate_bmi(weight,height):
    """Function to calculate BMI"""
    bmi = weight/(height**2)
    return round(bmi,2) # Round off ans to 2 decimal numbers.

def main():
    """First function to be called"""
    # Clear screen using module function.
    clear_screen_module.clear_screen()
    print("This script accepts weight & height, then calculates BMI.\n")
    # Accept numeric value only for weight and height using try-except.
    # If non-numeric value is entered, then exit the script.
    try:
        user_weight = eval(input("Enter weight in kg: "))
        user_height = eval(input("Enter height in meter: "))
    except NameError:
        print("The script accepts only numeric values. Exiting script now!")
        sys.exit(1)
    # Call function to calculate BMI.
    user_bmi = calculate_bmi(user_weight,user_height)
    print(f"\nYour BMI is: {user_bmi}")
    # Call function to classify BMI.
    user_bmi_category = classify_bmi(user_bmi)
    print(f"You fall in {user_bmi_category} category.\n")
    return None

# Call main function if the script is executed.

if __name__ == "__main__":
    main()
