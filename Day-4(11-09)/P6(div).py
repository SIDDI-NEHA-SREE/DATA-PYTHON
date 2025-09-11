#division using exception
def division(m,n):
    try:
        res = m / n
        print("Result is", res)
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        

n,m=map(int,input("Enter two numbers: ").split())
division(n,m)