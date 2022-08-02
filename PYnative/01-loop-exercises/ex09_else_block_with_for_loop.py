"""Module to demonstrate use of else block with for loop"""

# Same as the if statement, Python allows us to use an else block along with for loop.
# for loop can have the else block, which will be executed when the loop terminates normally.

import clear_screen_module

def main():
    """First function to be called"""
    clear_screen_module.clear_screen()
    print("This script prints \"Done!\" if the loop is executed without errors.")
    print("Press ENTER to proceed.")
    input()
    for eachnum in range(1,6,1):
        print(eachnum)
    else:
        print("Done!")
    print()

if __name__ == "__main__":
    main()
