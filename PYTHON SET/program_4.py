
set_var = {11,22,33,44,55}

print("value of set_var:",set_var)
print("no of balues in set_var:",len(set_var))

print("****** remove 33 from set *****")

set_var.remove(33)
print("value of set_var:",set_var)
print("no of balues in set_var:",len(set_var))

print("****** remove random value from set *****")

set_var.pop()
print("value of set_var:",set_var)
print("no of balues in set_var:",len(set_var))

print("****** remove all values from set *****")

set_var.clear()
print("value of set_var:",set_var)
print("no of balues in set_var:",len(set_var))