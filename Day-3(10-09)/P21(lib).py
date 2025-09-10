'''You are building a Library Management System in Python. The system should store books in a dictionary where:
Key → Book ID
Value → Book Title
Write a Python program to perform the following operations using Dictionaries:
Add a book to the library (Book ID, Title).
Remove a book using Book ID.
Search for a book by Book ID and display the title.
Update the title of a book (e.g., correction in title).
Display all books in the library.
Count the total number of books in the library.
Check if a book title exists in the library (reverse lookup).'''
def addbook(k,v):
    if k not in lib.keys():
        lib[k]=v
        return f"{k},{v} added to the library"
    else:
        return f"{k}-{v} already in library"
def removebook(k):
    if k not in lib.keys():
        return f"{k},{lib[k]} not in library"
    else:
        del lib[k]
        return f"{k}-{lib[k]} removed in library"
def searchbookID(k):
    if k not in lib.keys():
        return f"{k},{lib[k]} not in library"
    else:
        return f"{k}-{lib[k]}"
def searchbookT(v):
    if v not in lib.values():
        return f"{v} not in library"
    else:
        for key, val in lib.items():
            if val == v:
                return f"{v} Id-{key} "
def updatebook(k):
    if k not in lib.keys():
        return f"{k},{v} not in library"
    else:
        v=input("Enter the name for update: ")
        lib[k]=v
        return f"{k}-{v} updated in library"
def displaybook():
    return f"Id-Book: {lib}"
def countbook():
    return f"Ttal Books: {len(lib)}"


lib={}
print("1. Add book\n2. Remove book\n3. Search by id\n4. Display books\n5. Count books\n6.Update book\n7.search by title\n8.exit")
while(True):
    n=int(input("Enter your choice: "))
    if n==1:
        k,v=input("Enter id and name to add:").split()
        print(addbook(k,v))
    elif n==2:
        print(removebook(input("Enter id to remove: ")))
    elif n==3:
        print(searchbookID(input("Enter book ID to search: ")))
    elif n==4:
        print(displaybook())
    elif n==5:
        print(countbook())
    elif n==6:
        print(updatebook(input("Enter book ID to update: ")))
    elif n==7:
        print(searchbookT(input("Enter book name to search: ")))
    elif n==8:
        break
    else:
        print("Invalid")