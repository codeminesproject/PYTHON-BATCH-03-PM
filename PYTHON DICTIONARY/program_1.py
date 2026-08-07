
"""
Dictionary store value in key value format

Syntax:

variable_name = {"key":"value","key":"value",.....} 

"""

dict_var = {"id":1,"name":"CodeMines Computer","percentage":89.87,"institute_name":"Computer Institute"}

print(dict_var)
print("datatype of dict var:",type(dict_var))
print("no of values in dictionary:",len(dict_var))

print("*********** access values of dictionary *************")

print("value of id:",dict_var["id"])
print("value of name:",dict_var["name"])
print("value of percentage:",dict_var["percentage"])
print("value of institute_name:",dict_var["institute_name"])

print("*********** Show all keys from dictionary *************")

for key in dict_var.keys():
    print(key)

print("*********** Show all values from dictionary *************")

for val in dict_var.values():
    print(val)

print("*********** Access value from key from dictionary *************")

for key in dict_var.keys():
    print(f"value of {key}: {dict_var[key]}")

print("*********** Show all item (key value pair) from dictionary *************")

for val in dict_var.items():
    print(val)
