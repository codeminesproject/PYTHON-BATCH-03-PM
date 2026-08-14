
"""
variable: used to hold data temporory

Type of variable:
1. Global Variable
2. Local Variable

Global Variable: It is a variable which is declared at program level
In below example a and b declared at program level. hence they are global variable
global variable are accessible in entire program.


local variable: It is a variable declared inside a function.
In below example add variable eclared inside function addition. hence add is a local variable

"""

def addition(num_1,num_2):
    add = num_1 + num_2
    print("Addition:",add)
    print("Inside addition() - value of a:",a)
    print("Inside addition() - value of b:",b)

a = 10
b = 20

print("value of a:",a)
print("value of b:",b)

addition(a,b)
