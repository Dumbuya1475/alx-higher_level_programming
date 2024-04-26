#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
<<<<<<< HEAD
str = (str[39:67] + str[107:112] + str[0:6])
=======
str = str[39:67] + str[107:112] + str[:6]
>>>>>>> 69f966ee05059221ac9911ea4871ad8b5f77a395
print(str)
