# String Operations
# Reverse a string

#  Aniket -> tekinA

def ReverseString(s : str):
    rev = ""

    for char in s:
        rev = char + rev

    return rev

my_string = "Aniket"
print(f"\n Reverse a String")
print(ReverseString(my_string))