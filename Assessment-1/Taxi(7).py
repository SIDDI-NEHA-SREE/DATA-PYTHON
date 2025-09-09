def fare(d):
    if not d:
        return 0
    sum=0
    for i, j in enumerate(d, 1):
        f=50+(10*j)
        sum=sum+f
        print(f"Trip {i}: ${f}")
    print(f"Total Fare: ${sum}")

trips = [5, 10, 3]
fare(trips)