"""
Single Grand Parent -> Single Parent -> Single Child
"""

class GrandParent:
    def GrandParentFunction(self):
        print("This is Grand Parent Function")

class Parent(GrandParent):

    def ParentFunction(self):
        print("This is Parent Function")

class Child(Parent):

    def ChildFunction(self):
        print("This is Child Function")

child_obj = Child()
child_obj.ParentFunction()
child_obj.GrandParentFunction()
child_obj.ChildFunction()
