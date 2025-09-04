#real time current bill using functions
def realbill(n):
    a=50*3.80
    b=(50*3.80)+(50*4.20)
    c=(50*3.80)+(50*4.20)+(100*5.10)
    d=(50*3.80)+(50*4.20)+(100*5.10)+(100*6.30)
    if(n>=1 and n<=50):
        return n*3.80
    elif(n>=51 and n<=100):
        m=n-50
        return (a+(m*4.20))
    elif(n>=100 and n<=200):
        m=n-100
        return(a+b+(m*5.10))
    elif(n>=200 and n<=300):
        m=n-200
        return(a+b+c+(m*6.30))
    elif(n>300):
        m=n-300
        return(a+b+c+d+(m*7.50))
    else:
        return 0

cno = int(input("Enter Consumer number : ")) 
cname = input("Enter Consumer name : ")
pr,lr = map(float,input("Enter present month reading and last month reading sep with comma : ").split(","))   
msg = f"Name : {cname}\nNumber : {cno}\nPresent month reading : {pr}\nLast month reading : {lr}\nTotal readings : {(pr-lr)}"
print(msg)
print("Current Bill : ",realbill(pr-lr))