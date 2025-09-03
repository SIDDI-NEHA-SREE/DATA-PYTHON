# positive or negative
def Sign(n):
    if(n<0):
        print(f"{n}-Negative")
    elif(n>0):
        print(f"{n}-Positive")
    else:
        print(f"{n}-Zero")

Sign(int(input("Enter: ")))