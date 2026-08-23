
class Institute:

    institute_name = "CodeMines Computer Institute"
    mobile = "9167519953"
    email = "santtoshupadhyay@gmail.com"

    def StudentDetails(self,name,email,mobile):
        print("Student Name:",name)
        print("Student Email:",email)
        print("Student Mobile:",mobile)
        self.InstituteDetails()

    def InstituteDetails(self):
        print("Institute Name:",self.institute_name)
        print("Institute Mobile:",self.mobile)
        print("Institute Email:",self.email)

# create object for class Institute
obj = Institute()

# call StudentDetails
obj.StudentDetails("Aishwarya","aishwarya@gmail.com","1234567890")