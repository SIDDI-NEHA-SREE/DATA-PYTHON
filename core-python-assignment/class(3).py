class Student:
    def __init__(self, students):
        self.students = students
   
    def average(self):
        avg = {}
        for i, j in self.students.items():
            avg[i] = round(sum(j) / len(j), 2)
        return avg
   
    def Topper(self):
        avg = self.average()
        topper = max(avg, key=avg.get)
        return topper


students = {"John": [85, 78, 92], "Alice": [88, 79, 95], "Bob": [70, 75, 80]}
print(f"Average Marks: {Student(students).average()}")
print(f'Top Performer: "{Student(students).Topper()}"')