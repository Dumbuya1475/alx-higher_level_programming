#!/usr/bin/python3
<<<<<<< HEAD

def weight_average(my_list=[]):
    if not my_list:
        return 0
    num = 0
    den = 0
    for tup in my_list:
        num += tup[0] * tup[1]
        den += tup[1]
    return (num / den)
=======
def weight_average(my_list=[]):
    if my_list and len(my_list):
        num = 0
        dem = 0
        for tup in my_list:
            num += (tup[0] * tup[1])
            dem += tup[1]
        return (num / dem)
    return 0
>>>>>>> 69f966ee05059221ac9911ea4871ad8b5f77a395
