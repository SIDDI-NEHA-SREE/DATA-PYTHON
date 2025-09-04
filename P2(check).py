#write a program to input any character and check
#whether it is alphaet,digit or special character.
#use functions

def check(n):
    if(n.isalpha()):
        return "alphabet"
    elif(n.isdigit()):
        return "digit"
    else:
        return "special character"
    
def check1(n):
    if((n>'A' and n<'Z')or(n>'a' and n<'z')):
        return "alphabet"
    elif(int(n)>=0 and int(n)<=9):
        return "digit"
    elif(int(n)<0 or int(n)>9):
        return "Not a digit"
    else:
        return "special character"
    
print(check1(input("Enter any character : ")))
print(check(input("Enter any character : ")))