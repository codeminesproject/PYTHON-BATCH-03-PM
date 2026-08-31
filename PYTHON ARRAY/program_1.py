
"""

Array: It is a collection of element of same data type

syntax:

array_variable = array.array(datatype,[values_1,values_2,......])

"""

import array

arr_1 = array.array('i',[45,43,55,77,87,89,-11])
print(arr_1.tolist())

arr_2 = array.array('B',[45,43,55,77,87,89])
print(arr_2.tolist())

arr_3 = array.array('f',[34.65444,98.234567,67.123456])
print(arr_3.tolist())

arr_4 = array.array('d',[34.65444,98.234567,67.123456])
print(arr_4.tolist())

arr_5 = array.array('u',['a','e','i','o','u'])
print(arr_5.tolist())

arr_6 = array.array('w',['akshay','shankar','supriya','santtosh'])
print(arr_6.tolist())

