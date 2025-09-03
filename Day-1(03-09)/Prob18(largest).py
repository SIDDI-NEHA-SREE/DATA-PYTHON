#largest of three numbers
def largest(a,b,c):
    if(a>=b ):
        if(a>=c):
            return a
    elif(b>=a):
        if( b>=c):
            return b
    else:
        return c
    
a,b,c = map(float,input("Enter 3 values sep with comma : ").split(","))
print(f"{largest(a,b,c)} is largest")