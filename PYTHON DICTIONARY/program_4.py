dict_var = {"id":1,"name":"Amit Sharma","percentage":89.87,"institute_name":"Computer Institute"}

print(dict_var)
print("no of values in dictionary:",len(dict_var))

print("********** Type 1: Remove key percentage from dictionary ***********")

# del is keyword it is used to delete key value from dictionary

del dict_var["percentage"]
print(dict_var)
print("no of values in dictionary:",len(dict_var))

print("********** Type 2: Remove key institute_name from dictionary ***********")

dict_var.pop("institute_name")

print(dict_var)
print("no of values in dictionary:",len(dict_var))

print("****** remove last key value pair from dictionary ******")

dict_var.popitem()

print(dict_var)
print("no of values in dictionary:",len(dict_var))

print("****** remove all key value pair from dictionary ******")

dict_var.clear()

print(dict_var)
print("no of values in dictionary:",len(dict_var))
