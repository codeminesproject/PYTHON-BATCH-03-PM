
def addition(num_1,num_2,num_3=0,num_4=0):
    add = num_1 + num_2 + num_3 + num_4
    print("Addition:",add)

def greet(name="Guest"):
    print("Welcome:",name)

addition(20,30)
addition(100,200,300)
addition(150,250,350,450)

greet("CodeMines")
greet()