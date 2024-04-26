#!/usr/bin/python3
<<<<<<< HEAD

def multiply_by_2(a_dictionary):
    new_dict = {}
    for key, value in a_dictionary.items():
        new_dict.update({key: (value * 2)})
    return (new_dict)
=======
def multiply_by_2(my_dict):
    return {key: value * 2 for key, value in my_dict.items()}
>>>>>>> 69f966ee05059221ac9911ea4871ad8b5f77a395
