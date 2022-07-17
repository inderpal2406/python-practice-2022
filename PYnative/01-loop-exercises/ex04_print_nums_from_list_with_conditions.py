"""Module to print numbers from a list that satusfy certain conditions"""

# 1st condition: The num should be divisible by 5.
# 2nd condition: if num > 150, then skip it & move to next number.
# 3rd condition: if num > 500, then stop the loop.

# Import modules.

import clear_screen_module

# Define functions.

def main():
    """First function to be called"""
    clear_screen_module.clear_screen()
    print('''
    This script prints numbers from a list which satisfy below conditions,
    # 1st condition: The num should be divisible by 5.
    # 2nd condition: if num > 150, then skip it & move to next number.
    # 3rd condition: if num > 500, then stop the loop.
    ''')
    print("Press ENTER to proceed.\n")
    input()
    numbers = [12,75,150,180,145,525,50]
    print(f"numbers = {numbers}")
    for eachnum in numbers:
        if eachnum > 500:
            break
        if eachnum > 150:
            continue
        if eachnum%5 == 0:
            print(eachnum)
    # Using elif instead of if has same effect due to break & continue sentences being used.
    # We removed elif and used if to increase pylint rating.
    print() # Leave a space at the end.

# Call main() when the script is executed.

if __name__ == "__main__":
    main()
