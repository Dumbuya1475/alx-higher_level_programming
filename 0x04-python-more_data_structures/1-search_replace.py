#!/usr/bin/python3
<<<<<<< HEAD


def search_replace(my_list, search, replace):

    new_list = []
    for element in my_list:
        if element == search:
            new_list.append(replace)
        else:
            new_list.append(element)
    return (new_list)
=======
def search_replace(my_list, search, replace):
    def s_r_elm(elm):
        return (elm if elm != search else replace)
    return list(map(s_r_elm, my_list))
>>>>>>> 69f966ee05059221ac9911ea4871ad8b5f77a395
