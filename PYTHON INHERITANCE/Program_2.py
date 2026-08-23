

class Parent:

    def __init__(self):
        print("Parent Constructor Called")

    def ParentFunction(self):
        print("This is Parent Function")

class Child(Parent):

    def __init__(self):
        print("Child Constructor Called")

    def ChildFunction(self):
        print("This is Child Function")

child_obj = Child()
parent_obj=Parent()