"""
Class: It is a collection of properties likes methods and attibutes
class - It is a blueprint for a object

methods - it is a function declared inside a class
attibutes - variables declared inside a class

Syntax:

class classname:
    // properties of class

    
Object - It is used to exposed properties of class outside the class

Syntax of object:
object_name = classname()

self it is a keyword it is used when we want to acces property of class using object
"""

class Institute:
    def details(self):
        print("CodeMines Computer")

    def greet(self,name):
        print("Welcome: ",name)

    def faculty(self,name,educatio,mobile,email):
        print("Name: ",name)
        print("Education: ",educatio)
        print("Mobile: ",mobile)
        print("Email: ",email)

obj = Institute()
obj.details()
obj.greet("CodeMines")
obj.faculty("Santtosh Upadhyay","Mster in Data Science","9167519953","santtoshupadhyay@gmail.com")