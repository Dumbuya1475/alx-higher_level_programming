if __name__ == "__main__":
    import sys
    
    arg_v = len(sys.argv) -1
    
    if arg_v == 0:
        print("0 argument.")
    elif arg_v == 1:
        print("1 argument:")
    else:
        print("{} argument".format(arg_v))
    for check in range(arg_v):
        print("{}: {}".format(check + 1, sys.argv[check + 1]))