#search occurance
def soccur(str, s):
    c = list(str)
    d = []
    for i in range(len(c)):
        if c[i] == s:
            d.append(i)
    if d:
        return f"{s} occurred at positions {d}"
    else:
        return "not found"


str = input("Enter a string: ")
s = input("Enter to search: ")
print(soccur(str, s))