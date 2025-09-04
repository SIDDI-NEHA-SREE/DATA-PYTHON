#perfect - sum of divisors excluding number is same as number
def perfect(n):
    sum=0
    for i in range(1,n):
        if(n%i==0):
            sum=sum+i
    return (sum==n)

p=perfect(int(input("Enter n : ")))
print("Perfect")if (p) else print("Not Perfect")