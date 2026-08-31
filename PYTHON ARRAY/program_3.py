
import array

arr_1 = array.array('i',[])

size = int(input("Please enter no of values: "))

for i in range(0,size):
    values = int(input("Please enter value: "))
    arr_1.append(values)

print(arr_1)