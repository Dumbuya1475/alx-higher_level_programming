#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
<<<<<<< HEAD
    count = 0
    i = x

    for item in range(i):
        try:
            print(f"{my_list[item]}", end="")
            count += 1
        except IndexError:
            break
    print()
    return (count)
=======
    """Print x elememts of a list.

    Args:
        my_list (list): The list to print elements from.
        x (int): The number of elements of my_list to print.

    Returns:
        The number of elements printed.
    """
    ret = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            ret += 1
        except IndexError:
            break
    print("")
    return (ret)
 
>>>>>>> 69f966ee05059221ac9911ea4871ad8b5f77a395
