# find no of words aplabets and symbols
def string(str):
    c = str.strip().split()
    a,s,n=0,0,0
    for i in str:
        if i.isalpha():
            a=a+1
        elif i.isnumeric():
            n=n+1
        else:
            s=s+1
    return (f"Words-{len(c)} Alphabets-{a} Numbers-{n} Symbols-{s}")

print(string(input("Enter : ")))