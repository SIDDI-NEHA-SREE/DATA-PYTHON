def totalp(d):
    total = 0
    for price in d.values():
        total += int(price)
    return total

items = {}
n = int(input("Enter no of items: "))
for i in range(n):
    item, price = input(f"Enter item-{i} and price separated by space: ").split()
    items[item] = price

print("Total Price:", totalp(items))