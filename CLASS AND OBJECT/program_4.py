
"""
Encapsulation:
It is to apply restriction on properties of class, what to access and what not to access

Type of Encapsulation:
1. Public
2. private

In python if we start name of method or attribute with double underscore _ then is considered as a private property

"""

class Institute:

    institute_name = "CodeMines Computer Institute"
    mobile = "9167519953"
    email = "santtoshupadhyay@gmail.com"
    __balance=12345

    def StudentDetails(self,name,email,mobile):
        print("Student Name:",name)
        print("Student Email:",email)
        print("Student Mobile:",mobile)

    def InstituteDetails(self):
        print("Institute Name:",self.institute_name)
        print("Institute Mobile:",self.mobile)
        print("Institute Email:",self.email)
        print("Balance:",self.__balance)
        account_number = self.__BankDetails("InstituteDetails")
        if account_number == "1234567890":
            print("Student Authorised")
        else:
            print("Unauthorised student")

    def __BankDetails(self,request_name):
        return "1234567890"
        

obj = Institute()

obj.StudentDetails("Supriya","1234567890","supriya@gmail.com")
obj.InstituteDetails()

# we can not call private function directly from object
obj.__BankDetails()

# we can not call private variable directly from object
print("Balance:",obj.__balance)
