def percentage(rate):
    if not rate:
        return 0
    count = sum(1 for i in rate if i >= 4)
    return (count / len(rate)) * 100

ratings = [5, 4, 3, 5, 2, 4, 1, 5]
print(f"Positive Feedback: {percentage(ratings):.1f}%")