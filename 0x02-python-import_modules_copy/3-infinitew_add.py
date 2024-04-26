if __name__ == "__main__":
    import sys
    
    arg_v = len(sys.argv) -1
    
    if arg_v == 0:
        print(arg_v)
    else:
        for count in range(arg_v):
            add_arg = arg_v + count
            
            # print("{}")
            print("{}".format(add_arg))