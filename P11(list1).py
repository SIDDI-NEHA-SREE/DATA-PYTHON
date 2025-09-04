# list of x to y-1
def nlist(n,m):
    l=[]
    for i in range(n,m,2):
        l.append(i)
    return l

n,m=map(int,input("Enter n,m sep with comma : ").split(","))
print(nlist(n,m))