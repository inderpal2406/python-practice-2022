'''
This script will display nursery rhyme in below format,

Twinkle, twinkle, little star,
	How I wonder what you are! 
		Up above the world so high,   		
		Like a diamond in the sky. 
Twinkle, twinkle, little star, 
	How I wonder what you are
'''

# Import modules.

import platform
import os

# Detect OS type and clear the screen.

os_name=platform.system()
if os_name == "Windows":
    os.system("cls")
elif os_name == "Linux":
    os.system("clear")
else:
    print(f"This machine's OS is neither Windows nor Linux.")
    print(f"This script is designed only for Windows and Linux OS. Hence, exiting now.")

# Display purpose of the script.

print(f"This script will display a nursery rhyme for you. Press ENTER to proceed.\n")
input()

# Display the nursery rhyme.

print(f"Twinkle, twinkle, little star,\n\tHow I wonder what you are!")
print(f"\t\tUp above the world so high,\n\t\tLike a diamond in the sky.")
print(f"Twinkle, twinkle, little star,\n\tHow I wonder what you are!")
print(f"\nThat's it for now.")