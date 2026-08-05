
# create list using user input

size = int(input("Please enter no of values you want to insert in list: "))

list_var = []

for i in range(0,size):
    value = int(input("Please enter value: "))
    list_var.append(value)
    #list_var.insert(i,value)


print("****************************************")

print(list_var)