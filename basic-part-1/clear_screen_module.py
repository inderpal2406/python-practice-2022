# This script defines a custom module to clear the screen.
# This module/script can be imported into other scripts where there is a need to clear the screen.

# Import modules.

import platform
import os

# Define function to detect the OS type and clear the screen.

def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    elif platform.system() == "Linux":
        os.system("clear")
