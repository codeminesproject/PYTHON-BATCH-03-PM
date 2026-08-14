
"""
When we want to show single logic with return or print then we can use lambda function

Syntax:

function_name = lambda param_1,param_2 : logic



"""
add = lambda a,b : print("Addition:",a+b)

add(20,30)

greet =  lambda : print("Welcome to CodeMines")

greet()

sub = lambda a,b : a + b

sub_result = sub(50,70)
print("Subtraction:",sub_result)