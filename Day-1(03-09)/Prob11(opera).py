## perform all operators
def sum(a,b):
    return a+b
def dif(a,b):
    return abs(a-b)
def mul(a,b):
    return a*b
def div(a,b):
    if (b!=0):
        return a/b
    return -1
def floor(a,b):
    if(b!=0):
        return a//b
    return -1
def power(a,b):
    return a**b
def remain(a,b):
    return a%b
    
a,b=map(int,input("Enter a,b sep with comma").split(","))
print(sum(a,b))
print(dif(a,b))
print(mul(a,b))
print(div(a,b))
print(floor(a,b))
print(power(a,b))
print(remain(a,b))
