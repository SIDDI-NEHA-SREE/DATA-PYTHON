# count elements frequency 
def frequency(l):
    f = {}
    for i in l:
        if i in f:
            f[i] += 1
        else:
            f[i] = 1
    for key, value in f.items():
        print(key, "->", value)

l = [1, 3, 5, 7, -2, -5, -3, 6, -7]
frequency(l)