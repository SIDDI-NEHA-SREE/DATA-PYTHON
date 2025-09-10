#find no of vowes and conconents
def isvowel(str):
    c,v=0,0
    for i in str:
        if (i in ['a','e','i','o','u','A','E','I','O','U']):
            v=v+1
        else:
            c=c+1
    return (f"Vowels- {v} and Conconents- {c}")
print(isvowel(input("Enter a string: " )))