class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        return f"Employee : {self.name} - ${self.salary}"
    
class Manager(Employee):
    def __init__(self, name, salary, dep):
        super().__init__(name, salary)
        self.dep = dep

    def display(self):
        return f"Manager : {self.name} - ${self.salary}, Department: {self.dep}"


name = input("Enter name: ")
salary = int(input("Enter salary: "))
dep = input("Enter department: ")

s = Employee(name, salary)
d = Manager(name, salary, dep)

print(s.display())
print(d.display())
