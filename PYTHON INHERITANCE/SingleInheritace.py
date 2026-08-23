
"""
Single Parent Single Child
"""

class Parent:

    def ParentFunction(self):
        print("This is Parent Function")

class Child(Parent):

    def ChildFunction(self):
        print("This is Child Function")

child_obj = Child()
child_obj.ParentFunction()
child_obj.ChildFunction()