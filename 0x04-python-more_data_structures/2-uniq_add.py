#!/usr/bin/python3
<<<<<<< HEAD


def uniq_add(my_list=[]):
    new_list = []
    sum = 0
    for num in my_list:
        if num not in new_list:
            sum += num
            new_list.append(num)
    return (sum)
=======
def uniq_add(my_list=[]):
    add = 0
    for i in set(my_list):
        add += i
    return add
>>>>>>> 69f966ee05059221ac9911ea4871ad8b5f77a395
