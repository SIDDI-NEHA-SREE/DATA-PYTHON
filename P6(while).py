#print n natural numbers using while

def natural(n):
    while(n>0):
        print(n)
        n-=1

natural(int(input("Enter n : ")))

