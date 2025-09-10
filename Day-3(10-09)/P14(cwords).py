#count total no of words
def cwords(str):
    c = str.strip().split()
    return (f"Total words : {len(c)}")

print(cwords(input("Enter a sentence: ")))

