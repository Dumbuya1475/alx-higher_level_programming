c = 0

for letter in range(ord('z'), ord('a') -1, -1):
    print("{}".format(chr(letter - c)), end="")
    if c == 0:
        c = 32
    else:
        c = 0
    