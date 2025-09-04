#sum of natural numbers
def nsum(n):
    sum=0
    while(n>0):
        sum=sum+n
        n-=1
    return sum

print(nsum(int(input("Enter n : "))))