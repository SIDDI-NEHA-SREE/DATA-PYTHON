# vowels or consonants
def isvowel(n):
    if (n in ['a','e','i','o','u','A','E','I','O','U']):
        print(f"{n}-Vowel")
    else:
        print(f"{n}-Consonant")

isvowel(input("Enter a character: " ))