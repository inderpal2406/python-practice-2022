"""Module to find words with both alphabets & numbers in a sentence"""

import clear_screen_module

def find_alphanumeric_words(fnstr):
    """Function to find words with alphabets & numbers in a sentence"""
    wordlist = fnstr.split()
    fn_ans_wordlist = []
    for eachword in wordlist:
        for eachletter in eachword:
            if eachletter.isdigit():
                fn_ans_wordlist.append(eachword)
                break
    return fn_ans_wordlist

def main():
    """First function to be called"""
    clear_screen_module.clear_screen()
    print("This script finds words with both alphabets & numbers, in a sentence.")
    print("Press ENTER to proceed.")
    input()
    str1 = "Emma25 is a data scientist50 & AI expert."
    ans_wordlist = find_alphanumeric_words(str1)
    print(f"The string: {str1}")
    print("\nOutput:")
    for eachword in ans_wordlist:
        print(eachword)
    print() # Leave line at the end.

if __name__ == "__main__":
    main()
