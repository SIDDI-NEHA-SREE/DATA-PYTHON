'''volume of the cube
volume of the cylinder'''
pi=3.14
a=int(input("Enter the side of the cube: "))
print("Volume of the cube: ", a**3)
r,h = map(int,input("Enter radius and height of cylinder sep with comma:").split(","))
print("Volume of the cylinder: ",pi*(r**2)*h)