def safe_print_list(my_list=[], x=0):
    x = my_list
    
    try:
        print(x(len))
    except Exception:
        print("Error")

safe_print_list()
