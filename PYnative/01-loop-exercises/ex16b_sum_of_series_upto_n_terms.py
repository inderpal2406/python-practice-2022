"""Module to calculate sum of series upto n terms"""

# Import modules.

import sys
import clear_screen_module

# Define functions.

def SumOfSeriesOfNTermsOfNum(fn_num,fn_num_n):
    """Function to calculate sum of series of n terms of num"""
    fn_sum = 0
    for eachnumi in range(1,fn_num_n+1,1):
        fn_num_str = str(fn_num)
        strlist = []
        count = 1
        while count <= eachnumi:
            strlist.append(fn_num_str)
            count = count + 1
        final_str_num = ''.join(strlist)
        final_num = int(final_str_num)
        fn_sum = fn_sum + final_num
    return fn_sum

def main():
    """First function to be called"""
    clear_screen_module.clear_screen()
    print("""
    This script calculates sum of series upto n terms.
    If num=2 & n=5, then sum is calculated in below format,
    sum = 2 + 22 + 222 + 2222 + 22222
    """)
    try:
        num = int(input("Enter num: "))
        num_n = int(input("Enter n: "))
    except ValueError:
        print("Please enter an integer value only. Exiting script now!\n")
        sys.exit(1)
    if num <= 0 or num_n <=0:
        print("Please enter an integer greater than zero. Exiting script now!\n")
        sys.exit(1)
    totalsum = SumOfSeriesOfNTermsOfNum(num,num_n)
    print(f"Total sum: {totalsum}\n")

# Call main() when the script is executed.

if __name__ == "__main__":
    main()
