# leap yr or not
def leapyr(n):
    if((n%4==0 and n%100!=0)or( n%400==0)):
        print(f"{n}-Leap yr")
    else:
        print(f"{n}-Normal yr")

leapyr(int(input("Enter a year: ")))