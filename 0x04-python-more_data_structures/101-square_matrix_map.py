#!/usr/bin/python3
def square_matrix_map(matrix=[]):
<<<<<<< HEAD
    return (list(map(lambda x: list(map(lambda y: y**2, x)), matrix)))
=======
    return list(map((lambda row: list(map((lambda x: x * x), row))), matrix))
>>>>>>> 69f966ee05059221ac9911ea4871ad8b5f77a395
