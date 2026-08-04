
list_var = [99,43,23,67,1]

print("values of list:",list_var)
print("no of values in list:",len(list_var))

print("****** remove last value from list *****")

list_var.pop()
print("values of list:",list_var)
print("no of values in list:",len(list_var))

print("****** remove value 43 from list *****")

list_var.remove(43)
print("values of list:",list_var)
print("no of values in list:",len(list_var))

print("****** remove value from 1st position *****")

list_var.pop(1)
print("values of list:",list_var)
print("no of values in list:",len(list_var))

print("****** remove all values from list *****")

list_var.clear()
print("values of list:",list_var)
print("no of values in list:",len(list_var))