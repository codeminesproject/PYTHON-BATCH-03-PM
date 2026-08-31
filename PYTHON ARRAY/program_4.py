
import array

arr_1 = array.array('i',[23,11,-10,34,66])
print("values of array:",arr_1)

arr_2 = array.array('i',sorted(arr_1))
print(arr_2.tolist())

print("reverse array:")

arr_2.reverse()
print(arr_2.tolist())
