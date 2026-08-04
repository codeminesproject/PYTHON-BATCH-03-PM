
# Method 2 - Formatted Message

import sys

name = "CodeMines"

print(f"Value of variable name is {name}")
print(f"datatype of variable name is {type(name)}")
print(f"memory size of variable name is {sys.getsizeof(name)} byte")
print(f"Value of variable name is {name}, datatype of variable name is {type(name)} and memory size of variable name is {sys.getsizeof(name)} byte")

print("-----------------------------------------------------------------------------------------")

age = 123456

print(f"value of variable name age is {age}")
print(f"datatype of variable name age is {type(age)}")
print(f"memory size of variable name age is {sys.getsizeof(age)} byte")

print("-----------------------------------------------------------------------------------------")

percent = 456.76
print(f"value of variable percent is {percent}")
print(f"datatype of variable name percent is {type(percent)}")
print(f"memory size of variable percent is {sys.getsizeof(percent)} byte")

