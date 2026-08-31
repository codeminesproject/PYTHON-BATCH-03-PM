
import numpy as np


array_var = np.array([45,11,23,-1,90,76])

print("element of array:",array_var)
print("type of array:",type(array_var))
print("number of values in array:",len(array_var))

print("============ add value at end of list in array ==================")

array_var = np.append(array_var,101)
print("element of array:",array_var)

print("============ insert value 33 at position 3 list in array ==================")

array_var = np.insert(array_var,3,33)
print("element of array:",array_var)

print("============ delete value from 2nd position from array ==================")

array_var = np.delete(array_var,2)
print("element of array:",array_var)

print("=========== sort array in ascending order ==============")

array_var = np.sort(array_var)
print("element of array:",array_var)

print("=========== sort array in descending order ==============")

array_var = array_var[::-1]
print("element of array:",array_var)

print("=========== basic functionality of array ======================")

print("addition of array:",np.sum(array_var))
print("min of array:",np.min(array_var))
print("max of array:",np.max(array_var))
print("mean of array:",np.mean(array_var))