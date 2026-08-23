
"""
Single Parent Multiple Child
"""

class Parent:

    def ParentFunction(self):
        print("This is Parent Function")

class Child1(Parent):

    def Child1Function(self):
        print("This is Child 1 Function")

class Child2(Parent):

    def Child2Function(self):
        print("This is Child 2 Function")

child1_obj = Child1()
child1_obj.ParentFunction()
child1_obj.Child1Function()

child2_obj = Child2()
child2_obj.ParentFunction()
child2_obj.Child2Function()