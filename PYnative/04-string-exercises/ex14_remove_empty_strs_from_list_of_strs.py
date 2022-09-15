"""Module to remove empty strings from a list of strings"""

# Import modules.

import clear_screen_module

# Define functions.

def remove_empty_strings_from_list(fnstrlist):
    """Function to remove empty strings from the list if strings"""
    for eachstr in fnstrlist:
        if bool(eachstr) == False:  # Condition can be also "not bool(eachstr)"
            # Condition can be also "bool(eachstr) is False"
            # Pylint recommends above 2 commented conditions.
            empty_str_index = fnstrlist.index(eachstr)
            fnstrlist.pop(empty_str_index)
    return fnstrlist

def main():
    """First functiont to be called"""
    clear_screen_module.clear_screen()
    print("This script removes empty strings from a list of strings.")
    print("Press ENTER to proceed.")
    input()
    strlist = ["Emma","Jon","","Kelly",None,"Eric",""]
    print(f"Original list of strings: {strlist}")
    ans_strlist = remove_empty_strings_from_list(strlist)
    #print(f"Original list of strings: {strlist}")
    print(f"After removing empty strings: {ans_strlist}\n")
    # As var name is pointer to memory location where the var value is stored.
    # strlist, fnstrlist, ans_strlist - all point to same location.
    # As list is mutable, value gets updated at location due to pop operation.
    # So, all strlist, fnstrlist, ans_strlist now has updated value.
    # If we want to print previous string list after the operation, we won't be able to do so.
    # We need to read more on creating vars with same value but at different memory location.
    # copy & deepcopy functions from copy module may prove useful for this.
    # For now we'll print original str list before it gets operated on.
    # In this way, we may not need to return result to ans_strlist var, but we'll keep it for now.

# Call main() when the script is executed.

if __name__ == "__main__":
    main()
