#create a class and object: student details
#problem: create a student class to store a students name and roll number.create a object and display the details using an instance method.
class student:
    def __init__(self,name,roll_number):
        self.name=name
        self.roll_number= roll_number
    def display_details(self):
        print("name:",self.name)
        print("roll number:",self.roll_number)
s1=student("saurabh",1)
s1.display() 