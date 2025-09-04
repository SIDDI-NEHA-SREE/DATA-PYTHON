# list of 0 to x-1
def nlist(n):
    l=[]
    for i in range(0,n):
        l.append(i)
    return l

print(nlist(int(input("Enter n : "))))