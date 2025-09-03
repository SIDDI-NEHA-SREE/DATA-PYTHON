# arguments and return value
def kmtomiles(km):
    m=0.621*km
    return m

km=float(input("Enter Kilometers : "))
print(f"{km} kiolometes is {kmtomiles(km)} miles")
