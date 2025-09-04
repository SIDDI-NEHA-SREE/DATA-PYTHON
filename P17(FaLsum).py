#print sum of first and last digit of a number
def FaLsum(n):
    l=n%10
    while(n>=10):
        n=n/10
    f=round(n)
    print("Sum : ",(f+l))


FaLsum(int(input("Enter n: ")))