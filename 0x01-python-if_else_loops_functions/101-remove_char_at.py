#!/usr/bin/python3
<<<<<<< HEAD

def remove_char_at(str, n):
    str_cp = (str[0:n] + str[n+1:])

    if n < 0:
        return (str)
    return (str_cp)
=======
# Author - Godswill Kalu

def remove_char_at(str, n):
    if n < 0:
        return (str)
    return (str[:n] + str[n+1:])
>>>>>>> 69f966ee05059221ac9911ea4871ad8b5f77a395
