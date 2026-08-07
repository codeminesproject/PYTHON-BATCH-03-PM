
dict_var = {"id":1,"name":"CodeMines Computer","percentage":89.87,"institute_name":"Computer Institute"}

print(dict_var)
print("no of values in dictionary:",len(dict_var))

print("*********** Type 1: access values of dictionary *************")

print("value of id:",dict_var["id"])
print("value of name:",dict_var["name"])
print("value of percentage:",dict_var["percentage"])
print("value of institute_name:",dict_var["institute_name"])
#print("value of gender:",dict_var["gender"])

print("*********** Type 2: access values of dictionary *************")

print("value of id:",dict_var.get("id"))
print("value of name:",dict_var.get("name"))
print("value of percentage:",dict_var.get("percentage"))
print("value of institute_name:",dict_var.get("institute_name"))
print("value of gender:",dict_var.get("gender","key not found"))


