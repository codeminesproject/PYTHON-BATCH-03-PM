
"""
Multiple Parent Single Child
"""

class Parent1:

    def Parent1Function(self):
        print("This is Parent 1 Function")

class Parent2:

    def Parent2Function(self):
        print("This is Parent 2 Function")

class Child(Parent1,Parent2):

    def ChildFunction(self):
        print("This is Child Function")

child_obj = Child()
child_obj.Parent1Function()
child_obj.Parent2Function()
child_obj.ChildFunction()