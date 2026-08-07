
dict_var = {}

isContinue = "y"

while isContinue=="y":
    key = input("Please enter key: ")
    value_type = int(input("1 -> int, 2 -> float and anything for string: ")) 
    if value_type == 1:
        value = int(input(f"Please enter value for {key}:"))
    elif value_type == 2:
        value = float(input(f"Please enter value for {key}:"))
    else:
        value = input(f"Please enter value for {key}:")
    dict_var[key] = value
    isContinue = input("Press y to continue else press anything: ")

print(dict_var)