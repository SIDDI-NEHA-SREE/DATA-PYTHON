# print is prime or not using while
def prime(n):
    i=2
    while(i<n):
        if(n%i==0):
            print("Not Prime")
            break
        i+=1
    else:
        print("Prime")

prime(int(input("Enter n: ")))