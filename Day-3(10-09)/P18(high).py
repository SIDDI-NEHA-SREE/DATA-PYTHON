#•Write a Program to find highest frequency character in a string.
def hoccurences(str):
    f = {}
    for i in str:
        if i in f:
            f[i] += 1
        else:
            f[i] = 1
    v=max(f.values())
    result = [k for k, val in f.items() if val == v]
    return result, v
print(hoccurences(input("Enter a string: ")))