

class Parent:

    def ParentFunction(self):
        print("This is Parent Function")

    def address(self):
        print("This is parent address")

class Child(Parent):

    def ChildFunction(self):
        print("This is Child Function")
        # call address from child class
        self.address()

    def address(self):
        print("This is child address")

child_obj = Child()
child_obj.ChildFunction()