#!/usr/bin/python3

def magic_calculation(a, b):
    from magic_calculation_102 import add, sub

    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return (c)

<<<<<<< HEAD
    return(sub(a, b))
=======
<<<<<<< HEAD
    else:
        return(sub(a, b))
=======
<<<<<<< Updated upstream
    else:
        return(sub(a, b))

=======
    return(sub(a, b))
>>>>>>> Stashed changes
>>>>>>> 69f966ee05059221ac9911ea4871ad8b5f77a395
>>>>>>> main
