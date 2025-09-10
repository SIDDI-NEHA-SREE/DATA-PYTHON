'''You are building a simple E-commerce application in Python. 
The system should maintain a list of products available in the cart.
 Write a Python program to perform the following operations using Lists:
1.Add a product to the cart.
2.Remove a product from the cart 
3.Search for a product in the cart 
4.Display all products in the cart
5.Show the total number of products in the cart
 Cart Operations:
1. Add Product
2. Remove Product
3. Search Product
4. Display Cart
5. Count Products
6. Exit
Enter choice: 1
Enter product to add: Laptop
Product 'Laptop' added to cart.
Enter choice: 1
Enter product to add: Phone
Product 'Phone' added to cart.
Enter choice: 4
Cart: ['Laptop', 'Phone']
Enter choice: 3
Enter product to search: Phone
Yes, 'Phone' is in the cart.
Enter choice: 5
Total products in cart: 2'''

def addcart(n):
    if n not in cart:
        cart.append(n)
        return (f"Product '{n}' added to cart.")
    else:
        return (f"Product '{n}' already in cart.")
def removecart(n):
    if n in cart:
        cart.remove(n)
        return (f"Product '{n}' removed from cart.")
    else:
        return (f"Product '{n}' not in cart.")
def searchcart(n):
    if n in cart:
        return (f"Yes, '{n}' is in the cart")
    else:
        return (f"No, '{n} is not in the cart")
def displaycart():
    return (f"Cart: {cart}")
def countcart():
    return (f"Total products in cart: {len(cart)}")
def sortcart():
    cart.sort()
    return (f"Sorted cart : {cart}")
def clearcart():
    cart.clear()
    return (f"Cart is cleared - {cart}")

cart=[]
print(" Cart Operations:\n1. Add Product\n2. Remove Product\n3. Search Product\n4. Display Cart\n5. Count Products\n6. Sort\n7.clear cart\n8.exit")
while(True):
    n=int(input("Enter your choice: "))
    if n==1:
        print(addcart(input("Enter product to add: ")))
    elif n==2:
        print(removecart(input("Enter product to remove: ")))
    elif n==3:
        print(searchcart(input("Enter product to search: ")))
    elif n==4:
        print(displaycart())
    elif n==5:
        print(countcart())
    elif n==6:
        print(sortcart())
    elif n==7:
        print(clearcart())
    elif n==8:
        break
    else:
        print("Invalid")
    

