#print armstrong
def armstrong(n):
    sum=0
    m=n
    while(n!=0):
        r=n%10
        sum=sum+(r**3)
        n=n//10
    return (sum==m)

am=armstrong(int(input("Enter n : ")))
print("Armstrong")if (am==True) else print("Not Armstrong")