'''You are asked to build a simple E-commerce Billing System using Python modules.
Create a module file named ecommerce_utils.py that contains the following functions:
apply_discount(price, discount_percent) → applies a discount and returns the discounted price.
add_gst(price, gst_percent=18) → adds GST (default 18%) and returns the new price.
generate_invoice(cart, discount_percent=0, gst_percent=18) → accepts a dictionary cart 
(with product names as keys and prices as values) and prints a detailed invoice.
Create a main program file named main.py that:
Imports the ecommerce_utils module.
Creates a shopping cart (dictionary) with at least 3 products.
Calls the module functions to generate an invoice.
Expected Output Example:
------ INVOICE ------
Laptop          : ₹55000
Phone           : ₹30000
Headphones      : ₹2000
---------------------
Subtotal: ₹87000
After 10% discount: ₹78300.0
After 18% GST: ₹92454.00
---------------------
Thank you for shopping with us!'''
def apply_discount(price, dp):
    return price-(price*(dp/100))
def add_gst(price, gst_percent=18):
    return price+(price*(gst_percent/100))
def generate_invoice(cart, discount_percent=0, gst_percent=18):
    print("------ INVOICE ------")
    for key, val in cart.items():
        print(f"{val}    : ₹{key}")
    print("---------------------")
    print(f"Subtotal : ₹{sum(cart.values())}")
    print(f"After 10% discount: ₹{apply_discount(sum(cart.values()), 10)}")
    print(f"After 18% GST: ₹{add_gst(sum(cart.values()), gst_percent=18)}")
    print("---------------------")
    print("Thank you for shopping with us!")
        

