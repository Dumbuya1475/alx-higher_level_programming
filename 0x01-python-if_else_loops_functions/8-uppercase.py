#!/usr/bin/python3
<<<<<<< HEAD

def uppercase(str):
    for a in str:
        if ord(a) >= 97 and ord(a) <= 122:
            a = chr(ord(a) - 32)
        print("{}".format(a), end="")
=======
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
>>>>>>> 69f966ee05059221ac9911ea4871ad8b5f77a395
    print("")
