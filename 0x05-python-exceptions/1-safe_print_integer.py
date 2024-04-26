#!/usr/bin/python3

def safe_print_integer(value):
<<<<<<< HEAD
=======
    """Print an integer with "{:d}".format().

    Args:
        value (int): The integer to print.

    Returns:
        If a TypeError or ValueError occurs - False.
        Otherwise - True.
    """
>>>>>>> 69f966ee05059221ac9911ea4871ad8b5f77a395
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
