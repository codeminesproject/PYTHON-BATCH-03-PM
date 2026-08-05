"""
We can not modify values of tuple once created
"""

tuple_var = (89,76,45,11,67,89,76,89)

print("values of tuple:",tuple_var)
print("datatype of tuple:",type(tuple_var))

print("****** Step 1: Convert tuple into list *****")

# list is a class used to convert tuple into list

list_var = list(tuple_var)
print("values of list:",list_var)
print("datatype of list:",type(list_var))

print("****** Step 2: perform modification ******")

list_var.insert(3,101)
print("values of list:",list_var)

print("**** Step 3: Convert list into tuple ***")

tuple_var = tuple(list_var)
print("values of tuple:",tuple_var)
print("datatype of tuple:",type(tuple_var))