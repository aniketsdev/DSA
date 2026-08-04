# Print Name N times using Recursion
# Problem Description: Given an integer N, write a program to print your name N times.

# Input: N = 3
# Output: Ashish Ashish Ashish 
# Explanation: Name is printed 3 times.
# Input: N = 1
# Output: Ashish 
# Explanation: Name is printed once.
class Solution:

    def printName(self , name, N):
        
        # if count == N:
        #     return
        
        # print(name)

        # self.printName(name, count + 1, N)

        if N <= 0:
            return 
        
        print(name)

        self.printName(name, N-1)


# Print 1 to N using Recursion
# Problem Description: Given an integer N, write a program to print numbers from 1 to N.

    def printNumber(self , N , start):
        if start == N:
            return
        
        print(start+1)
        
        self.printNumber(N, start+1)

    def printNto1(self, N):
        
        if N == 0:
            return
        
        print(N)

        self.printNto1(N-1)
        
# Sum of first N Natural Numbers
# Problem Statement: Given a number ‘N’, find out the sum of the first N natural numbers .
    def sumOfNumber(self ,N):
        # if start == N:
        #     print("Sum is of N ", sum)
        #     return

        # # print("sum is", sum, start)
        # sum = sum + start

        # self.sumOfNumber(N, start + 1, sum)
        # print("0000000",N)
        if N == 0:
            return 0
        
        return N + self.sumOfNumber(N-1)

# Factorial of a given number
# You are given an integer n. Return the value of n! or n factorial.
# Factorial of a number is the product of all positive integers less than or equal to that number.

# Example 1
# Input: n = 2
# Output: 2
# Explanation: 2! = 1 * 2 = 2.

    def factorial(self, n):
        if n == 0 or n == 1:
            return 1
        # print("iiiiiii", n)
        return n * self.factorial(n-1)

# Reverse a given Array
# Input: N = 5, arr[] = {5,4,3,2,1}
# Output: {1,2,3,4,5}
# Explanation: Since the order of elements gets reversed the first element will occupy the fifth position, the second element occupies the fourth position and so on.

# Input: N=6 arr[] = {10,20,30,40}
# Output: {40,30,20,10}
# Explanation: Since the order of elements gets reversed the first element will occupy the fifth position, the second element occupies the fourth position and so on.

    def reverseArray(self, arr):
        # brute force approach
        # reverseArr = []
        # n = len(arr)
        # for i in range(n):
        #     # print(n-i-1)
        #     print("bbbbbbb", arr[n-i-1])
        #     reverseArr.append(arr[n-i-1])
        
        # return reverseArr
        # Better Approach
        # n = len(arr)
        # p1 = 0
        # p2 = n-1

        # while p1 < p2:
        #     arr[p1], arr[p2] = arr[p2], arr[p1]
        #     p1 += 1
        #     p2 -= 1
        
        # return "Reverse Array is : ", arr
    
        # reverseArr = []
        n = len(arr)

        # for i in range(n):
        #     print("test",arr[n-i-1])
        #     reverseArr.append(arr[n-i-1])

        # return reverseArr

        # p1 = 0
        # p2 = n-1

        # while p1 < p2:
        #     arr[p1], arr[p2] = arr[p2], arr[p1]
        #     p1+=1
        #     p2-=1

        # return arr

        # Built in methods for Array
        return arr[::-1]

    #  Check if the given String is Palindrome or not
    # Example 1:
    # Input: Str =  “ABCDCBA”
    # Output: Palindrome
    # Explanation: String when reversed is the same as string.

    # Example 2:
    # Input: Str = “TAKE U FORWARD”
    # Output: Not Palindrome
    # Explanation: String when reversed is not the same as string.

    def checkPalindromeNumber(self, str):
        # left = 0
        # right = len(str) - 1
        # flag = False

        # while left <= right:
        #     if str[left] == str[right]:
        #         flag = True
        #         print("Test", str[left], str[right])
        #     else :
        #         flag = False

        #     left+=1
        #     right-=1


        # return flag

        left = 0
        right = len(str) - 1
        flag = True

        while left < right:
            if not str[left].isalnum():
                left+=1

            elif not str[right].isalnum():
                right+=1

            elif str[left].lower() != str[right].lower():
                return "Not Palindrome"

            else:
                left+=1
                right-=1

        return "Palindrome"    
        
        # Optimze solution using recurssion
    
    def checkPalindromeNumberUsingRecurssion(self, i, s):
        # Base Condition

        if i > len(s) // 2:
           return True

        if s[i] != s[len(s) - i - 1]:
            return False

        return self.checkPalindromeNumberUsingRecurssion(i+1, s)



if __name__ == "__main__":
    N = 5
    rawN = "abcba"
    arr = [10,20,30,40]

    name = "Aniket"
    print(f"/n N times of Name ")
    sol = Solution()
    result = sol.printName(name, N)
    result2 = sol.printNumber(N, 0)
    result3 = sol.printNto1(N)
    print("\n Sum Of N Numbers")
    result4 = sol.sumOfNumber(N)
    result5 = sol.factorial(N)
    result6 = sol.reverseArray(arr)
    result7 = sol.checkPalindromeNumber(rawN)
    result8 = sol.checkPalindromeNumberUsingRecurssion(0, rawN)
    
    print(f"{result}, \n {result2} , \n {result3} \n {result4} \n {result5}, \n {result6}, \n {result7} \n {result8}")