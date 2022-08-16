"""Module to copy all content of a file into another file by skipping specific line"""

# Import modules.

import os
import clear_screen_module

# Define functions.

def copycontent(fn_srctextfile,fn_desttextfile,fn_skiplinenum):
    """Func to copy content of one file to another & skip a line in this process"""
    fileobj = open(fn_srctextfile,"r")
    contentlist = fileobj.readlines()
    #print(f"{contentlist}")    # Each line has \n in it already.
    count = 0
    newfileobj = open(fn_desttextfile,"w")
    for eachitem in contentlist:
        count = count + 1
        if count == fn_skiplinenum:
            continue
        newfileobj.write(eachitem)
        #count = count + 1  # this works till 5 but doesn't increment beyond it,
        #because of the continue statement. Hence, count is moved up in the block.
    newfileobj.close()
    print(f"Content of {fn_srctextfile} copied to {fn_desttextfile}.")
    print(f"Line number {fn_skiplinenum} is skipped during copy.")

def check_and_create_file(fn_foldername,fn_srctextfile):
    """Function to check existence of file & create it"""
    if not os.path.exists(fn_foldername):
        os.mkdir(fn_foldername)
        print(f"Folder {fn_foldername} created.")
    else:
        print(f"Folder {fn_foldername} already exists.")
    if not os.path.exists(fn_srctextfile):
        fileobj = open(fn_srctextfile,"a")
        count = 1
        while count <= 10:
            fileobj.write(f"Line {count}.\n")
            count = count + 1
        fileobj.close()
        print(f"File {fn_srctextfile} created.")
    else:
        print(f"File {fn_srctextfile} already exists.")

def main():
    """First function to be called"""
    clear_screen_module.clear_screen()
    foldername = "txt-files"
    srctextfile = "txt-files\\test.txt"
    desttextfile = "txt-files\\new_file.txt"
    skiplinenum = 5
    print(f"""
    This script copies content of {srctextfile} to {desttextfile} by skipping
    line number {skiplinenum} from source file during copy. Press ENTER to proceed.
    """)
    input()
    check_and_create_file(foldername,srctextfile)
    copycontent(srctextfile,desttextfile,skiplinenum)

if __name__ == "__main__":
    main()
