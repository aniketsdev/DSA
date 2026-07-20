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
    def sumOfNumber(self ,N, start, sum):
        if start == N:
            print("Sum is of N ", sum)
            return

        # print("sum is", sum, start)
        sum = sum + start

        self.sumOfNumber(N, start + 1, sum)


if __name__ == "__main__":
    N = 5
    name = "Aniket"
    print(f"/n N times of Name ")
    sol = Solution()
    result = sol.printName(name, N)
    result2 = sol.printNumber(N, 0)
    result3 = sol.printNto1(N)
    print("\n Sum Of N Numbers")
    result4 = sol.sumOfNumber(N+1, 0, 0)
    
    print(f"{result}, \n {result2} , \n {result3} \n {result4}")