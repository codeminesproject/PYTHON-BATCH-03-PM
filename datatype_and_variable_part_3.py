
# type is a class used to display variable datatype

# sys is a module (library) used to show memory utilisation of variable
import sys

name = "CodeMines"
print(name)
print(type(name)) # <class 'str'> means datatype of name is string
print(sys.getsizeof(name))


age = 123456
print(age)
print(type(age)) # <class 'int'> means datatype is integer
print(sys.getsizeof(age))

percent = 456.76
print(percent)
print(type(percent)) # <class 'float'> means datatype is float
print(sys.getsizeof(percent))