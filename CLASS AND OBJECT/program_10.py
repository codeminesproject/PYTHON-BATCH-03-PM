class Institute:

    institute_name:str
    contact_number:str

    # Paramterised Constructor
    def __init__(self,p_name,p_number):
        self.institute_name = p_name
        self.contact_number = p_number

    def details(self):
        print("value of institute name:",self.institute_name)
        print("value of contact number:",self.contact_number)


name = input("Please enter institute name: ")
number = input("Please enter contact number: ")    

obj = Institute(name,number)
obj.details()