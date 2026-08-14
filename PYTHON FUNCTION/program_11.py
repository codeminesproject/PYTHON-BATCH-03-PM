
def addition(*args):
    add = 0
    for val in args:
        add += val
    print("Addition:",add)

addition(20,30)
addition(100,200,300)
addition(150,250,350,450)

addition()

