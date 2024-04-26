#!/usr/bin/python3
<<<<<<< HEAD


def square_matrix_simple(matrix=[]):
    new_matrix = []
    for col in matrix:
        result = list(map(lambda x: x**2, col))
        new_matrix.append(result)
    return (new_matrix)
=======
def square_matrix_simple(matrix=[]):
    return [list(map((lambda x: x * x), elm)) for elm in matrix]
>>>>>>> 69f966ee05059221ac9911ea4871ad8b5f77a395
