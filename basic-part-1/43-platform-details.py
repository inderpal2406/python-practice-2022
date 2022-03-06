# This script will display the OS name and OS release information.

# Import modules.

import platform
import clear_screen_module

# Define functions.

def main():
    # Clear the screen.
    clear_screen_module.clear_screen()
    # Display the purpose of the script.
    print(f"This script will display OS name and release information.\n")
    os_name = platform.system()
    os_release = platform.release()
    print(f"The OS name is: {os_name}")
    print(f"The OS release is: {os_release}\n")

# Main code starts here.

if __name__ == "__main__":
    main()
