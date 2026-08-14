"""
Function: It is a collection of statement which will only execute when it is called.

Type of functions:
1. Pre Defined Function:
2. User Defined Function:

Pre Defined Function: It is a function which defination is already known by interpreter
example: print(), input(), len(), min(), max(), sum()

User Defined Function: It is a function which is created by user as per its requirement

Syntax:

def function_name():
    collection of statements

def is a keyword which is used to define a function
function_name can be anything as per user but it should follow naming rules:

# function name can be anything but as per function name rules

1. function name always start from alpha character (a to z) and special character underscore _ only
2. function name should not contains any special character except underscore _
3. function name should not start from number 
4. function name can be combination of special character underscore _, alpha character and 
number
5. function name can not be keywords (pre defined words)

Type of functions:
1. Zero Parameterised function
2. Parameterised Function
3. Function With Return Statement
4. lamba function
5. recursive function

"""


def addition():
    num_1 = 10
    num_2 = 20
    add = num_1 + num_2
    print("addition:",add)


def subtraction():
    num_3 = 100
    num_4 = 50
    sub = num_3 - num_4
    print("subtraction:",sub)

def division():
    num_7 = 15
    num_8 = 3
    div = num_7 / num_8
    print("division:",div)

def multiplication():
    num_5 = 5
    num_6 = 6
    mul = num_5 * num_6
    print("multiplication:",mul)

addition()
subtraction()
multiplication()
division()

