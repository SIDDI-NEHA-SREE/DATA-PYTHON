def additem(m):
    if m in menu:
        print(f"{m} is available")
    else:
        menu.append(m)
def removeitem(m):
    if m in menu:
        menu.remove(m)
    else:
        print(f"{m} is not available")
def check(m):
    if m in menu:
        print(f'Availability: "{m} is available"')
    else:
        print(f'Availability: "{m} is not available"')


menu= ["Pizza", "Burger", "Pasta", "Salad"]
additem(input("Add-item: "))
removeitem(input("Remove-item: "))
print("Updated menu: ",menu)
check(input("Check-item: "))