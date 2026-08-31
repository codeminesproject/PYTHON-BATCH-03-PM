import numpy as np

array_var = np.array([45,11,23,-1,90,76])

print("values of array:",array_var.tolist())
print("length of array:",len(array_var))
print("datatype of array:",type(array_var))

print("----------------------------------------------")

print("value at 0 position:",array_var[0])
print("value at 1 position:",array_var[1])
print("value at 2 position:",array_var[2])
print("value at 3 position:",array_var[3])
print("value at 4 position:",array_var[4])
print("value at 5 position:",array_var[5])

print("----------------------------------------------")

for i in range(0,len(array_var)):
    print(array_var[i])

print("----------------------------------------------")

for value in array_var:
    print(value)