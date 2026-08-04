
name = "            CodeMines Computer             "

print("value of variable name:",name)
print("no of character in variable name:",len(name))

print("--- remove all additional space from name -------")

name_without_space = name.strip()
print("value of variable name_without_space:",name_without_space)
print("no of character in variable name_without_space:",len(name_without_space))

print("--- remove only left additional space from name -------")

name_without_space = name.lstrip()
print("value of variable name_without_space:",name_without_space)
print("no of character in variable name_without_space:",len(name_without_space))

print("--- remove only right additional space from name -------")

name_without_space = name.rstrip()
print("value of variable name_without_space:",name_without_space)
print("no of character in variable name_without_space:",len(name_without_space))

