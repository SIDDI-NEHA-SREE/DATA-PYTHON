#find len without using len(), compare without using compare(), concate without usimg concate
def length(n):
    c=0
    for i in n:
        c=c+1
    return c
def scompare(n,m):
    if n[:]==m[:]:
        return (f"{n} and {m} are same")
    else:
        return (f"{n} and {m} are not same")
def sconcate(n,m):
    return n+" "+m

str=input("To find length enter: ")
print(f"{str} - {length(str)}")
n,m=(input("Enter two words to compare: ").split(" "))
print(f"Compare({n} , {m})- {scompare(n,m)}")
a,b=input("Enter two words to concate: ").split(" ")
print(f"Concate({a} , {b})- {sconcate(a,b)}")