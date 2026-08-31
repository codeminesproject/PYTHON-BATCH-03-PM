
import array

arr_1 = array.array('i',[45,23,98,98,23])
print("values of array:",arr_1)

print("---- add 101 in array ---")

arr_1.append(101)
print("values of array:",arr_1)

print("---- add 202 in array ---")

arr_1.insert(1,202)
print("values of array:",arr_1)

print("---- update 303 at 3rd position in array ---")

arr_1[3]=303
print("values of array:",arr_1)

print("========== remove last element from array ===============")

arr_1.pop()
print("values of array:",arr_1)

print("========== remove 1st position element from array ===============")

arr_1.pop(1)
print("values of array:",arr_1)

print("========== remove 45 from array ===============")

arr_1.remove(45)
print("values of array:",arr_1)

print("========== reverse array ===============")

arr_1.reverse()

print("reverse:",arr_1)

print("========== add list into array ===============")

list_var = [34,35,36]
arr_1.extend(list_var)
print("values of array:",arr_1)