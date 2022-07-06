"""Module of a game to guess a random number"""

# Import modules.

import sys
import time
import random
import clear_screen_module

# Define functions.

def main():
    """First function to be called"""
    index = 1
    while index > 0:
        clear_screen_module.clear_screen()
        print('''
        In this game, you would enter start & end number of a range.
        Then a random number would be generated in that range.
        You would be given 3 guesses to guess the random number.
        If you could guess the number correctly, then you win.
        Press ENTER to proceed.\n
        ''')
        input() # Take ENTER key input to proceed.
        try:
            startnum = int(input("Enter the start number of the range: "))
            endnum = int(input("Enter the end number of the range: "))
        except ValueError:
            print("Please enter an integer value only. Exiting game now!\n")
            sys.exit(1)
        print("\nGenerating the random number...")
        time.sleep(3)
        randomint = random.randint(startnum,endnum)
        print("Random number generated.\n")
        iternum = 3
        while iternum > 0:
            try:
                userguess = int(input(f"Guess the random number generated between {startnum}-{endnum}: "))
            except ValueError:
                print("Please enter an integer value only. Exiting game now!\n")
                sys.exit(1)
            if userguess == randomint:
                print(f"Your guess is correct. Random number generated is {randomint}.\n")
                break
            else:
                iternum = iternum - 1
                print(f"Wrong guess. You have {iternum} chances left.Press ENTER to proceed.\n")
                input()
        if iternum == 0:
            print(f"You exhausted all 3 chances. Random number generated was: {randomint}\n")
        userchoice = input("Do you want to play one more time? [y|n]: ")
        if userchoice.casefold() == "y":
            continue
        elif userchoice.casefold() == "n":
            break
        else:
            print("Invalid choice. Please enter [y|n] only. Exiting game now.\n")
            sys.exit(1)

# Call main() when the script is executed.

if __name__ == "__main__":
    main()
