#print students who scored highest and students who scored above 75. use tuple and functions
'''A school stores student records as tuples in the format (roll_no, name, marks).
Write a Python program to:
Store the data of 5 students in a list of tuples.
Print the name of the student who scored the highest marks.
Print all students who scored more than 75 marks.'''
def topper(t):
    maxs = max(i[2] for i in t)
    return [i[0] for i in t if i[2] == maxs]
def s75(t):
    return [s[0] for s in t if s[2] > 75]


t=(['Siddi','5f5',80],['Neha','23b',74],['Sree','81a',90],['Varun','098',90],['Tharun','765',73])
print(f"Topper : {topper(t)}")
print(f"Above 75: {s75(t)}")
