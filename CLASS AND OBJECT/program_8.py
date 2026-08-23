
"""
Generators: classmethod and staticmethod
"""

class Institute:

    address = "Bhayander East"

    def details(self):
        print('Normal Function With Self')
        print("value of address:",self.address)

    @staticmethod
    def InstituteDetails():
        print("Institute Name: CodeMines Computer Institute")
        # in staic method we can not call global variable or other property of class
        # print("value of address:",address)

    @classmethod
    def FacultyDetails(cls):
        print("Faculty Name: Santtosh Upadhyay")
        print("value of address:",cls.address)
        cls.details()

# call static method
Institute.InstituteDetails()

# call class method
Institute.FacultyDetails()