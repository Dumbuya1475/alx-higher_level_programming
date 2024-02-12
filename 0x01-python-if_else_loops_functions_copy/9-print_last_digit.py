#!/usr/bin/python3
# Author - Mohamed Super Dumbuya

def print_last_digit(number):
    """
    Print last digit
    - number: print
    """
    print(abs(number) % 10, end="")
    return (abs(number) % 10)
