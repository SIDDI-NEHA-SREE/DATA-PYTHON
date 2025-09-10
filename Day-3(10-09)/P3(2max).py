#find the 2nd max in the list
def max_2(l):
    f=l[0]
    s=l[1]
    for i in l:
        if i > f:
            s = f
            f = i
        elif i > s and i != f:
            s = i
    return s

l=[1,3,5,7,-2,-5,-3,8,-7]
print(max_2(l))