# This script will determine if the python shell is being executed by a 32-bit or 64-bit architecture processor.
# The platform module is used here.
# The Platform module is used to retrieve as much possible information about the platform on which the program is being currently executed.

# Import modules.

import platform
import clear_screen_module

# Define functions.

def main():
    # Clear the screen.
    clear_screen_module.clear_screen()
    # Display the purpose of the script.
    print(f"This script will determine the architecture of the processor running this script.\n")
    architecture = platform.architecture()[0]   # Determine the architecture.
    print(f"The architecture of processor running this script is: {architecture}\n")

# Main code starts here.

if __name__ == "__main__":
    main()
