#print first and last digit of a number
def FaLdigit(n):
    l=n%10
    print(l)
    while(n>=10):
        n=n/10
    print(round(n))


FaLdigit(int(input("Enter n: ")))