#palindromes in range
def palindrome(n,m):
    for i in range(n,m+1):
        if str(i)==str(i)[::-1]:
            print(i)

n,m=map(int,input("Enter the range: ").split(" "))
palindrome(n,m)