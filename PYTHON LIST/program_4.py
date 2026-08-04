
list_var = [99,43,23,67,1]

print("values of list:",list_var)
print("no of values in list:",len(list_var))

print("****** add 101 in a list ******")

list_var.append(101)
print("values of list:",list_var)
print("no of values in list:",len(list_var))

print("****** add 202 at 2nd position in a list ******")

list_var.insert(2,202)
print("values of list:",list_var)
print("no of values in list:",len(list_var))

print("****** add 303,404,505 in a list ******")

list_var.extend([303,404,505])
print("values of list:",list_var)
print("no of values in list:",len(list_var))