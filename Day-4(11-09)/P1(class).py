#create a class
class Person:
    def __init__(self,name,rollno,marks):
        self.name=name
        self.rollno=rollno
        self.marks=marks
    def display(self):
        return (f"Student: {self.name},{self.rollno},{self.marks}")

students = [] 
for i in range(2):
    print(f"Enter details of Student {i+1}:")
    name = input("Enter name: ")
    rollno = input("Enter roll no: ")
    marks = int(input("Enter marks: "))
    s = Person(name, rollno, marks)
    students.append(s)
for s in students:
    print(s.display())
