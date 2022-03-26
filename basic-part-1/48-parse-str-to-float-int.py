# This script has a pre-defined string which will be typecasted to float and integer.

# Import modules.

import clear_screen_module
import time

# Define functions.

def main():
    # Clear the screen.
    clear_screen_module.clear_screen()
    # Display purpose of the script.
    print(f"This script has a pre-defined string which will be converted to float and integer.\n")
    predef_str = "2.486"
    print(f"The pre-defined string is: {predef_str}\nIt's data type: {type(predef_str)}\n")
    time.sleep(1)
    print(f"Converting pre-defined string to float data type...")
    time.sleep(2)
    float_data = float(predef_str)
    print(f"The value after conversion to float is: {float_data}\nNew data type: {type(float_data)}\n")
    time.sleep(1)
    print(f"Converting float data to integer data type...")
    time.sleep(2)
    int_data = int(float_data)
    print(f"The value after conversion to integer is: {int_data}\nNew data type: {type(int_data)}\n")
    time.sleep(1)
    print(f"Completed the type casting of data. That's it for now. Be happy :)")
    return None

# Main code starts here.
if __name__ == "__main__":
    main()
