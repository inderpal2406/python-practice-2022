# This script has a pre-defined list.
# The elements of the list will be all concatenated into a string which would be displayed.

# Import modules.

import clear_screen_module

# Define functions.

def main():
    # Clear the screen.
    clear_screen_module.clear_screen()
    # Display purpose of the script.
    print(f"The elements of a pre-defined list would be concatenated into a string in this script.\n")
    # Define our list.
    our_list = ["a","e","#","i","o","u","@","ght"]  # We can have only str elements in the list as join method woould accept only str arguments.
    # Display our pre-defined list.
    print(f"The pre-defined list is: {our_list}\n")
    # Calculate length of list to be used to loop through each list element using the index of element.
    len_of_list = len(our_list)
    # Define empty string for join method. This empty string would be inserted in elements of list in the string using join method.
    empty_string = ""
    # Define another empty string which will hold resultant string of each iteration until all elements are concatenated.
    iterable_string = ""
    # Concatenate the list elements using a for loop and join method.
    for i in list(range(0,len_of_list,1)):
        iterable_string = empty_string.join([iterable_string,our_list[i]])
    print(f"The string formed by concatenating all list elements is as below,\n{iterable_string}")

# Main code starts here.

if __name__ == "__main__":
    main()
