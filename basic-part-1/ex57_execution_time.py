"""Module to calculate execution time"""

# This script calculates execution time in H:M:S format.

# Import modules.

import time
import datetime
import clear_screen_module

# Define functions.

def calculate_time_difference(time2,time1):
    """Function to calculate time difference"""
    time_format = "%H:%M:%S"
    # Get new datetime parsed from the strings time2, time1.
    time2 = datetime.datetime.strptime(time2,time_format)
    time1 = datetime.datetime.strptime(time1,time_format)
    # Get time interval in %H:%M:%S
    time_interval = time2 - time1
    return time_interval

def add_first_n_nums(n):
    """Function to add first n numbers"""
    ans = 0
    for i in list(range(1,n+1,1)):
        ans = ans + i
    return ans

def main():
    """First function to be called"""
    # Clear screen using module function.
    clear_screen_module.clear_screen()
    print("This script calculates execution time of complete script.")
    print("We'll calculate sum of first 10 crore numbers and the execution time for this.\n")
    # Start time.
    start_time = time.time()
    # Call function to add first n numbers.
    our_sum = add_first_n_nums(100000000)
    # End time.
    end_time = time.time()
    # Convert start & end time from epoch format to H:M:S format.
    # Start and end time is now in float format.
    start_time = datetime.datetime.fromtimestamp(start_time).strftime("%H:%M:%S")
    end_time = datetime.datetime.fromtimestamp(end_time).strftime("%H:%M:%S")
    # Start and end time is in string format now.
    # Call function to calculate execution time.
    exec_time = calculate_time_difference(end_time,start_time)
    print(f"Sume of first 100 numbers: {our_sum}")
    print(f"Time taken for calculation: {exec_time}\n")
    return None

# Call main() function when this script is executed.

if __name__ == "__main__":
    main()
