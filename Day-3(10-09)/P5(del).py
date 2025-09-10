def delete(x):
    if x in range(len(l)+1) :
        l[:] = l[:x] + l[x+1:]
    else:
        print("Invalid position")
    return l

l = [1, 3, 5, 7, -2, -5, -3, 6, -7]
print(l)
print(delete(int(input("Enter position : "))))