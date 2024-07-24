#Checking a Character is a vowel or consonant in Python

#Method :1
c = 'a'

# checking for vowels
if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u' or c == 'A' or c == 'E' or c == 'I' or c == 'O' or c == 'U':
    print(c, "is a vowel")  # condition true input is vowel
else:
    print(c, "is a consonant")  # condition true input is consonant


# -----------------------------------------------------------

# Method :2

# single function for both uppercase and lowercase
def isVowel(c):
    # converts to uppercase if it wasn't already
    c=c.upper()
    # returns true if char matches any of below
    return c == 'A' or c == 'E' or c == 'I' or c == 'O' or c == 'U'
c = 'f'

# show error message if c is not an alphabet
if not c.isalpha():
    print("Non alphabet")
elif isVowel(c):
    print(c, "is a Vowel")
else:
    print(c, "is a consonant")