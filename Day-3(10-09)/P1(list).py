def addele(n):
    #l.append(x)
    l=[]
    for i in range(n+1):
        x=input(f"Enter an element {i}: ")
        l+=[x]
    return l

n=int(input("Enter n: "))
print(addele(n))