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
    sign = False

    if n <= 0 :
        sign = True
        abs(n)
    
    while n > 0:
        # print("----", n)
        lastDigit = n % 10
        reverse = reverse * 10 + lastDigit
        n = n // 10
    
    return reverse

print(f"\n Reverse a Number \n")
print(ReverseNumber(1289))


# Count digits in a number
# Example 1:
# Input:N = 12345
# Output:5
# Explanation:  The number 12345 has 5 digits.

def CountDigit(n: int):    
    count = 0
    while n > 0:
        count += 1
        n = n // 10

    return count

print(f"\n Count Digit  \n")
print(CountDigit(123450293))

# //Check if a number is Palindrome or Not
# Problem Statement: Given an integer N, return true if it is a palindrome else return false.
def palindromeNumber(n : int):
    reverse = 0
    lastDigit = 0
    original = n
    
    while n > 0 :
        # print(n)
        lastDigit = n % 10
        reverse = lastDigit + reverse * 10
        n = n // 10
    
    if reverse == original:
        return True
    
    return False

print(f"/n Palindrome number /n")
print(palindromeNumber(101))

# Print all Divisors of a given Number
# A divisor of an integer N is a positive integer that divides N without leaving a remainder. In other words, if N is divisible by another integer without any remainder, then that integer is considered a divisor of N.

class Solution:
    def divisorOfNumber(self , n):
        divisor = []

        for i in range(1, n+1):
            if n % i == 0:
                divisor.append(i)
        
        return divisor

sol = Solution()
N = 12
result = sol.divisorOfNumber(N)
print(f"/n Print all Divisors of a given Number ")
print(result)