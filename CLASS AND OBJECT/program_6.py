
class Institute:

    institute_name = "CodeMines Computer"

    def details(self):
        print("CodeMines Computer")

    def faculty(name,educatio,mobile,email):
        print("Name: ",name)
        print("Education: ",educatio)
        print("Mobile: ",mobile)
        print("Email: ",email)

    
# access property of class without class object
Institute.faculty("Santtosh Upadhyay","Mster in Data Science","9167519953","santtoshupadhyay@gmail.com")

print("value of institute_name",Institute.institute_name) 