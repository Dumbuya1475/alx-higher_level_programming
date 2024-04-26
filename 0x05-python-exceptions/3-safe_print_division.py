#!/usr/bin/python3

def safe_print_division(a, b):
<<<<<<< HEAD
    try:
        c = a / b
    except (TypeError, ZeroDivisionError):
        c = None
    finally:
        print("Inside result: {}".format(c))
    return (c)
=======
    """Divides 2 integers and prints the result.."""
    try:
        div = a / b
    except (TypeError, ZeroDivisionError):
        div = None
    finally:
        print("Inside result: {}".format(div))
    return (div)
>>>>>>> 69f966ee05059221ac9911ea4871ad8b5f77a395
