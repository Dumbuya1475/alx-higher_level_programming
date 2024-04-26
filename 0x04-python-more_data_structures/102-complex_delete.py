#!/usr/bin/python3
<<<<<<< HEAD

def complex_delete(a_dictionary, value):
    list_keys = list(a_dictionary.keys())

    for value_dic in list_keys:
        if value == a_dictionary.get(value_dic):
            del a_dictionary[value_dic]

    return (a_dictionary)
=======
def complex_delete(my_dict, value):
    keys_to_del = []
    for key in my_dict:
        if my_dict[key] == value:
            keys_to_del.append(key)
    for key in keys_to_del:
        del my_dict[key]
    return my_dict
>>>>>>> 69f966ee05059221ac9911ea4871ad8b5f77a395
