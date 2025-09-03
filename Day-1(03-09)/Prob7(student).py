'''write a pgrm to enter student number,student name,3 subject marks, calculate total
avg and print all details'''
id = input("Enter ID : ")
sname = input("Enter Name : ")
a, b, c = map(float,input("Enter 3 subject marks sep with comma : ").split(","))
print("Name : ",sname)
print("ID : ",id)
print("S1 : ",a,"\nS2 : ",b,"\nS3 : ",c)
print("Total : ",(a+b+c))
avg = ((a+b+c)/3)
print("Avg : ",round(avg,2))

