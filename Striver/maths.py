# Count all Digits of a Number
# Subscribe to TUF+

# Hints

# Company
# You are given an integer n. You need to return the number of digits in the number.

# The number will have no leading zeroes, except when the number is 0 itself.

# Example 1
# Input: n = 4
# Output: 1

# Explanation: There is only 1 digit in 4.

# Example 2
# Input: n = 14
# Output: 2

# Explanation: There are 2 digits in 14.

def CountAllDigits(n : int):
    count = 0

    if n < 0:
        return 0
    
    while n > 0 :
        count+=1
        n = n//10
    
    return count

print(f"\nCount All Digits \n")
print(CountAllDigits(234))


# Reverse Digits of A Number

# Problem Statement: Given an integer N return the reverse of the given number.

# Note: If a number has trailing zeros, then its reverse will not include them. For e.g , reverse of 10400 will be 401 instead of 00401.

def ReverseNumber(n: int):
    reverse = 0
    lastDigit = 0
    isNegative = False

    if n < 0 :
        isNegative = True
        n = abs(n)
    
    while n > 0:
        lastDigit = n % 10
        reverse = reverse * 10 + lastDigit
        n = n // 10
    
    return -reverse if isNegative else reverse

print(f"\n Reverse a Number \n")
print(ReverseNumber(-1200))