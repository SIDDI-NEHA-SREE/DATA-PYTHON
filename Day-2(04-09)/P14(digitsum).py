#print sum of digits
def digitsum(n):
    sum=0
    while(n!=0):
        r=n%10
        sum=sum+r
        n=n//10
    return sum

ds=digitsum(int(input("Enter n : ")))
print("Sum of digits : ",ds)
