#!/usr/bin/python3
# Author - Mohamed Super Dumbuya

def uppercase(str):
    """
    Print a string in uppercase.
    - str - to be printed
    """
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            c = chr(ord(c) - 32)
        print("{}".format(c), end="")
    print("")
