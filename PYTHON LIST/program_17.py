
# create list using user input

size = int(input("Please enter no of values you want to insert in list: "))

list_var = []

for i in range(0,size):
    value_type = int(input("1 -> int, 2 -> float and anything for string: ")) 
    if value_type == 1:
        value = int(input(f"Please enter int value at {i} position: "))
    elif value_type == 2:
        value = float(input(f"Please enter float value at {i} position: "))
    else:
        value = input(f"Please enter string value at {i} position: ")
    list_var.append(value)
    #list_var.insert(i,value)


print("****************************************")

print(list_var)