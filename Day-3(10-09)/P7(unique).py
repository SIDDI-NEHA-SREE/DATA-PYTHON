#print unique element in list
def duplicate(l):
    m=[]
    for i in l:
        if i not in m:
            m.append(i)
    return m

l=[1,3,5,7,-2,5,3,6,-7]
print(duplicate(l))