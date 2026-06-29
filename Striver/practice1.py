# Print the numbers from 10 down to 1.
def isNumberReverse(n: int):
    for i in range(n):
        print(n-i)

print("Print Number 10 to 1")
print(isNumberReverse(10))


# Ask the user for a number n and print all numbers from 1 to n.

def isPrintAll(n: int):
    for i in range(1, n+1):
        print(i)

print("print all from 1 to n")
print(isPrintAll(5))

# Count how many vowels (a, e, i, o, u) are in a word entered by the user.


print("print vowels in word")
print(isPrintAll(5))

# Calculate the factorial of a number.
def fact(n: int):
    if n <=1:
        return 1
    return n * fact(n-1)

print("Factorial")  
print(fact(6))

# Reverse a string using a for loop (don't use slicing [::-1]).
def reverseString(string):
    reversed_text = ""
    for char in string:
        reversed_text = char + reversed_text
    
    return reversed_text

str = "demo"
print("Reverse a string")
print(reverseString(str))