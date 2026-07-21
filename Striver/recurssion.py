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
        n = len(arr)
        p1 = 0
        p2 = n-1

        while p1 < p2:
            arr[p1], arr[p2] = arr[p2], arr[p1]
            p1 += 1
            p2 -= 1
        
        return "Reverse Array is : ", arr
    
    # 
    

            
            

if __name__ == "__main__":
    N = 5
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

    
    print(f"{result}, \n {result2} , \n {result3} \n {result4} \n {result5}, \n {result6}")