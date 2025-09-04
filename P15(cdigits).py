#count no of digits in a number
def cdigits(n):
    c=0
    while(n!=0):
        r=n%10
        c+=1
        n=n//10
    return c

cd=cdigits(int(input("Enter n: ")))
print("Digits : ",cd)