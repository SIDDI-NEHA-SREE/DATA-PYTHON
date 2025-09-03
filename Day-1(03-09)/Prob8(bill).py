'''write a program to enter consumer(c) number ,cname,present month current reading,
previous month reading,calculate total units and current bill.cost per unit is 3.80.
 print all details with bill'''
cno = int(input("Enter Consumer number : "))
cname = input("Enter Consumer name : ")
pr,lr = map(float,input("Enter present month reading and last month reading sep with comma : ").split(","))
msg = f"Name : {cname}\nNumber : {cno}\nPresent month reading : {pr}\nLast month reading : {lr}\nTotal readings : {(pr-lr)}"
print(msg)
print("Current Bill : ",((pr-lr)*3.80))

