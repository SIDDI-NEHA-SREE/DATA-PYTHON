def bookseat(seat):
    if seat > ts or seat in bs:
        print("Seat unavailable.")
    else:
        bs.append(seat)
        print(f"{seat}-booked.")

def cancelseat(seat):
    if seat in bs:
        bs.remove(seat)
        print(f"Seat {seat} cancelled.")
    else:
        print("Seat not booked.")

def availableseats():
    return [i for i in range(1, ts + 1) if i not in bs]

ts=int(input("Total seats: "))
bs = [2, 5, 7] #bs=[]
#bs = list(map(int, input("Enter booked seats: ").split()))
bookseat(int(input("Enter to book: ")))
cancelseat(int(input("Enter to cancel: ")))
print(f"Available seats: {availableseats()}")