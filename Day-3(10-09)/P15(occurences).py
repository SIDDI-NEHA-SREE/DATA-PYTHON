#count occurences of a characters
def occurences(str):
    f = {}
    for i in str:
        if i in f:
            f[i] += 1
        else:
            f[i] = 1
    for key, value in f.items():
        print(key,value,end=',')

occurences(input("Enter a string: "))