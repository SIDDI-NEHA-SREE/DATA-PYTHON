# arguments but no return value
def daystoyr(d):
    m=round((d/30),0)
    y=round((m/12),0)
    mn=round((m-(y*12)),0)
    print(f"{d} days is {y} yr and {mn} months ")

d=int(input("Enter days : "))
daystoyr(d)


