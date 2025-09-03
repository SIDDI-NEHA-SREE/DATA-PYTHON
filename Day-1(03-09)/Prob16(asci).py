# check whether the character is alphabet or not
def check(n):
    if(n.isalpha()):
        print(f"{n}-alphabet")
    else:
        print(f"{n}-not an alphabet")

check(input("Enter: "))