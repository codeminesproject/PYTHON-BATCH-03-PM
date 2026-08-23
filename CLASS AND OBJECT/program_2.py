
"""
variable declared inside a class is called attribute
"""

class Institute:

    institute_name = "CodeMines Computer institute"

    def details(self):
        print("CodeMines Computer")
        address = "Bhayander East"
        # access global attribute of class institute_name inside function
        print("details() - value of variable institute_name:",self.institute_name)
        print("details() - value of variable address:",address)

    def greet(self):
        print("greet() - value of variable institute_name:",self.institute_name)

obj = Institute()
obj.details()

# access global attribute of class using object
print("value of variable institute_name:",obj.institute_name)

# update value of global variable institute_name
obj.institute_name = "CodeMines Computer"

obj.greet()