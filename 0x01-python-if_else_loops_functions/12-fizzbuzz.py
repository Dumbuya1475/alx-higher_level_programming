#!/usr/bin/python3
<<<<<<< HEAD

def fizzbuzz():
=======
# Author - Mohamed Super Dumbuya
def fizzbuzz():
    """Print the numbers from 1 to 100 separated by a space.
    """
>>>>>>> 69f966ee05059221ac9911ea4871ad8b5f77a395
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz ", end="")
        elif number % 3 == 0:
            print("Fizz ", end="")
        elif number % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(number), end="")
