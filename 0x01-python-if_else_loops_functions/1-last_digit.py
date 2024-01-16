#!/usr/bin/python3
import random
remainderber = random.randint(-10000, 10000)
remainder = abs(remainderber) % 10

if remainderber < 0:
    remainder = -remainder
print(f"Last remainder of {remainderber:d} is {remainder:d} and is ", end="")
if remainder > 5:
    print("greater than 5")
elif remainder == 0:
    print("0")
else:
    print("less than 6 and not 0")
