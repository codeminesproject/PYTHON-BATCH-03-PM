"""
Constructor is a special type of funtion which automatically called when object of class created
Only one constructor for a class

__init__ is a constructor

Type of constructor:
1. Default Constructor
2. Parameterised Constructor

"""

class Institute:

    # Default Constructor
    def __init__(self):
        self.details()

    def details(self):
        print("CodeMines Computer")

    

obj = Institute()