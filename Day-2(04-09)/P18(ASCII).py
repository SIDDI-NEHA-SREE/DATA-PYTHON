#print all ASCII characters with their values
def Cascii():
    for i in range(0,257):
        print(i," -> ",chr(i))

Cascii()
#for only keyboard values
def Cascii1():
    for i in range(48,57):
        print(i," -> ",chr(i))
    for i in range(65,91):
        print(i," -> ",chr(i))
    for i in range(97,122):
        print(i," -> ",chr(i))
    
Cascii1()
