# divisible by 11 and 5
def divisible11_5(n):
    if(n%11==0 and n%5==0):
        print("Divisible by 11 and 5")
    else:
        print("Not Divisible by 11 and 5")

divisible11_5(int(input("Enter: ")))