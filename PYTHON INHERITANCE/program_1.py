
"""
Parent -> Child
Base -> Derived
Super -> Sub

In inheritance we always create object of child class

Inheritance:
1. Single Inheritance
2. Hierarchical Inheritance
3. Multilevel Inheritance
4. Multiple Inheritance
5. Hybrid Inheritance

"""

class Institute:

    def about(self):
        print("Institute Name: CodeMines Computer Institute")
        print("Mobile Number: 9167519953")
        print("Address: Bhayander East")

    def __BankDetails(self):
        print("Account Number: 123xxxxxxxxx789")
        print("Password: xxxxxxxxxxxx")

class Students(Institute):

    def StudentDetails(self):
        print("This function used to provide student details")
        self.about()

    def StudentFees(self):
        print("This function used to provide student fees details")



student_obj = Students()
student_obj.StudentDetails()
student_obj.about()