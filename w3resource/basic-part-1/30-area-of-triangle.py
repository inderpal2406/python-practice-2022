# This script will accept height and base of a triangle and print its area.

# Import modules.

import clear_screen_module

# Define functions.

def calculate_area(b,h):
    result = 0.5*b*h
    return result

def main():
    # Clear the screen.
    clear_screen_module.clear_screen()
    # Display purpose of the script.
    print(f"The script will accept base and height of the triangle and then display its area.\n")
    # Accept the base and height of the triange and exit the script if user doesn't provide either an int or float number.
    try:
        base = eval(input("Enter the base of the triangle: "))
        height = eval(input("Enter the height of the triangle: "))
    except NameError:
        print(f"This script will accept only an integer or float value, which you have not provided. Hence, exiting script.")
        exit(1)
    except Exception as e:  # To catch any other exception than NameError.
        print(e)
        print(f"Please enter only an integer or float number. Exiting script now as incompatible input is provided!")
        exit(1)
    # As eval() can accept boolean values without error, check if bool value is not provided. If yes, then exit the script.
    if type(base) == bool or type(height) == bool:
        print(f"You have provided a boolean value which can't be processed. Please enter only an integer or float number. Exiting script now!")
        exit(1)
    # Calculate area of triangle.
    area = calculate_area(base,height)
    # Display area of the triangle.
    print(f"Area of triangle is: {area}")
    return None

# Main code starts here.

if __name__ == "__main__":
    main()
    