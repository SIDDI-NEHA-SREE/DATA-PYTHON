#calculate simple interest
p,t,r=map(float,input("Enter principal amount,time, rate of interest sep with comma :").split(","))
print("Simple interest amount : ",((p*t*r)/100))
print("Amount in hand:",(p+((p*t*r)/100)))