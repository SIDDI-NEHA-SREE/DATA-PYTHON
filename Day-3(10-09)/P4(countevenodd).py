def countevenodd(l):
    c,d=0,0
    for i in l:
        if i%2==0:
            c=c+1
        else:
            d=d+1
    return c,d

l=[1,3,5,7,-2,-5,-3,6,-7]
print("Even-odd",countevenodd(l))
