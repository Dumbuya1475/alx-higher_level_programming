#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE

remainder = number % 10

TEXT = "Last digit of " + str(number) + " is " + str(remainder)

if remainder > 5:
    print(TEXT + " and is greater than 5")
elif remainder == 0:
    print(TEXT + " and is 0")
else:
    print(TEXT +" and is less than 6 and not 0")
