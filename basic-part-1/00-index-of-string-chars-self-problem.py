# script to accept a string from user and display each of it's character along with its index number

# importing modules

import os
import platform
import sys

# clearing screen as per the OS

if platform.system()=="Windows":
  os.system("cls")
elif platform.system()=="Linux":
  os.system("clear")
else:
  print(f"Operating system couldn't be identified! Exiting script!")
  sys.exit(1)

# accepting user input string

user_str=input("Please enter a string value : ")

# initialize a variable to track index value

index=0

# looping through the string and displaying output

print(f"\nThe characters of string and their respective index values are as follows:\n")

for i in user_str:
  print(f"{i}\t-->>\t{index}")
  index+=1

# display last statement and exit script

print(f"\nThat's all folks!")