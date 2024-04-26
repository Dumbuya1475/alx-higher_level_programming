#!/usr/bin/python3
<<<<<<< HEAD

def best_score(a_dictionary):
    if a_dictionary:
        my_list = list(a_dictionary.keys())
        score = 0
        leader = ""
        for i in my_list:
            if a_dictionary[i] > score:
                score = a_dictionary[i]
                leader = i
        return (leader)
=======
def best_score(my_dict):
    if my_dict and len(my_dict):
        max = list(my_dict.keys())[0]
        for key in my_dict:
            if my_dict[key] > my_dict[max]:
                max = key
        return max
    return None
>>>>>>> 69f966ee05059221ac9911ea4871ad8b5f77a395
