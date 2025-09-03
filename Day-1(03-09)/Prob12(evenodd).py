# even or odd with conditioal statements
def evenodd(n):
    if(n%2==0):
        print(f"{n}-Even")
    else:
        print(f"{n}-Odd")

n=int(input("Enter: "))
evenodd(n)