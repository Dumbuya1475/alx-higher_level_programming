#!/usr/bin/python3
<<<<<<< HEAD

def print_sorted_dictionary(a_dictionary):
    keyes = list(a_dictionary.keys())
    keyes.sort()
    for key in keyes:
        print("{}: {}".format(key, a_dictionary[key]))
=======
def print_sorted_dictionary(my_dict):
    for key in sorted(my_dict.keys()):
        print("{:s}: {}".format(key, my_dict[key]))
>>>>>>> 69f966ee05059221ac9911ea4871ad8b5f77a395
