#no arguments but return value
def kmtomiles():
    km=float(input("Enter Kilometers : "))
    m=0.621*km
    return m

print(f"{kmtomiles()} miles")