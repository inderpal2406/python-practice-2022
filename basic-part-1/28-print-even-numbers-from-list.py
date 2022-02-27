# This script would iterate through each element of a pre-defined list of numbers and print 
# the even numbers from the list. 
# The script will stop immediately if the number 237 comes in the list and won't print the 
# further even numbers.

# Import modules.

import clear_screen_module

# Define the functions.

def main():
    # Clear the screen.
    clear_screen_module.clear_screen()
    # Display the purpose of the script.
    print(f"This script would print even numbers from a pre-defined list of numbers.")
    print(f"The script will stop if 237 comes as an element of the script and won't print the further even numbers after 237 in the list.\n")
    # Define our list of numbers.
    num_list = [
        386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
        399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
        815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
        958,743, 527
    ]
    # Display the pre-defined list.
    print(f"The pre-defined script is as below,\n{num_list}\n")
    # Display the even numbers from the list.
    print(f"The even numbers from the list are as below,")
    for i in num_list:
        if i == 237:
            print(f"\n\nThe script has encountered 237 number at index {num_list.index(237)}.")
            print(f"Hence, further even numbers beyond 237 won't be printed.")
            break   # Come out of loop to stop printing the even numbers after 237.
        elif i%2 == 0:
            print(f"{i}, ",end="")

# Main code starts here.

if __name__ == "__main__":
    main()
