def element_at(my_list, idx):
    if idx < 0:
        return None
    list_len = len(my_list)
    if idx > list_len:
        return None
    else:
        element = my_list[idx]
        return element