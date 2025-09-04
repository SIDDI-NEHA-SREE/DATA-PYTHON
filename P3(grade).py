# student grade
def grade(n):
    if(n>=40):
        if (n>80):
            return "Distension"
        elif(n<=80 and n>=71):
            return "A"
        elif(n<=70 and n>=51):
            return "B"
        else:
            return "C"
    else:
        return "Fail"

print(grade(int(input("Enter marks : "))))