# write aprogram enter weeek number and display week name
#usinf elif and functions
def week(n):
    if(n==1):
        return "Sunday"
    elif(n==2):
        return "Monday"
    elif(n==3):
        return "Tuesday"
    elif(n==4):
        return "Wednesday"
    elif(n==5):
        return "Thursday"
    elif(n==6):
        return "Friday"
    elif(n==7):
        return "Saturday"
    else:
        return "Invalid"
    
print(week(int(input("Enter a day : "))))