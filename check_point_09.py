# 1. IndexError
mylist = [14, "hello", 967]
# Error: the list has only 3 elements.
# The available indexes are 0, 1 and 2.
print(mylist[2])
# 2. Import Pandas and NumPy
# Error: module names are written in lowercase.
import pandas
import numpy
# 3. SyntaxError
# Error: print() needs parentheses.
print("python errors")
# 4. KeyError
mydictionnary = {True: "hello", False: "bye", '3': "python"}
# Error: 'True' is a string, but True is a boolean.
print(mydictionnary[True])
# 5. IndentationError
i = 14
while i < 78:
    # Error: the instructions inside the while loop must be indented.
    print(i)
    i += 1
# 6. StopIteration
it = iter([1, 2, 3])
print(next(it))
print(next(it))
print(next(it))
# Error: there are only 3 elements.
try:
    print(next(it))
except StopIteration:
    print("There are no more elements.")
# 7. TypeError
# Error: we cannot add a string and an integer.
result = 15 + 15
print(result)
# 8. ValueError
# Error: "python" cannot be converted into an integer.
result = int("15")
print(result)
# 9. NameError
# Error: the variable python was not defined.
python = "Python"
print(python)
# 10. ZeroDivisionError
# Error: we cannot divide by zero.
x = 19 / 1
print(x)