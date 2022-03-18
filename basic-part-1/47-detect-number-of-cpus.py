# This script will determine number of CPUs on the system.

# Import modules.

import clear_screen_module
import multiprocessing

# Define functions.

def main():
    # Clear the screen.
    clear_screen_module.clear_screen()
    # Display purpose of the script.
    print(f"This script will determine number of CPUs on the system.\n")
    num_of_cpus = multiprocessing.cpu_count()
    print(f"Number of CPUs: {num_of_cpus}\n")
    return None

# Main code starts here.

if __name__ == "__main__":
    main()
