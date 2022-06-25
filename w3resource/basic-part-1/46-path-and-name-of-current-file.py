# This script will print the path and name of the current file being executed.

# Import modules.

import clear_screen_module
import sys  # Needed to operate with command line arguments using sys.argv var which is a list of CLI args.
import os   # Needed to extract the dirname and name from complete path of our current file.

# Define functions.

def main():
    # Clear the screen.
    clear_screen_module.clear_screen()
    # Display purpose of the script.
    print(f"This script will print path and name of current file being executed.\n")
    complete_path = sys.argv[0]
    directory_path = os.path.dirname(complete_path)
    name_of_file = os.path.basename(complete_path)
    print(f"Current file is located in below directory:\n{directory_path}\n")
    print(f"Current file's name is as below:\n{name_of_file}\n")
    return None

# Main code starts here.
if __name__ == "__main__":
    main()
