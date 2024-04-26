#!/usr/bin/python3

import sys
<<<<<<< HEAD
def safe_print_integer_err(value):

    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, NameError, ValueError):
=======


def safe_print_integer_err(value):
    """Prints an integer with "{:d}".format().

    If a ValueError message is caught, a corresponding
    message is printed to standard error.

    Args:
        value (int): The integer to print.

    Returns:
        If a TypeError or ValueError occurs - False.
        Otherwise - True.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
>>>>>>> 69f966ee05059221ac9911ea4871ad8b5f77a395
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)
