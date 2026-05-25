# Pattern - 7: Star Pyramid 
# Problem Statement: Given an integer N, print the following pattern : N = 5


# Star Pattern 

#      *
#     ***
#    *****
#   *******
#  *********


# def starPattern(n : int):
#     t = 0
#     for i in range(n):
#         t += 1
#         for j in range(n-i):
#             print(" ",end="")
#         for k in range(i+t):
#             print("*", end="")
        
#         print()

def starPattern(n : int):
    for i in range(n):
        print(" " * (n-i), end="")
        print("*" * (2 * i + 1))


print(f"\n Star Pattern \n")
print(starPattern(5))



# Pattern - 8: Inverted Star Pyramid

# Problem Statement: Given an integer N, print the following pattern : N = 5

# *********
#  *******
#   *****
#    ***
#     *

# def invertedStarPattern(n : int):
#     t = 0
#     for i in range(n):
#         t +=1
#         for m in range(i):
#             print(" ", end="")
#         for j in range(n-i):
#             print("*", end="")
#         for k in range(j):
#             print("*", end="")
#         print()

def invertedStarPattern(n : int):
    for i in range(n):
        print(" " * i, end="")

        print("*" * (n-i), end="")
        
        print("*" * (n-i-1))

print(f"\n Inverted Star Pyramid \n")
print(invertedStarPattern(5))

# Pattern - 9: Diamond Star Pattern

# Problem Statement: Given an integer N, print the following pattern : N = 5

#  Diamond Star Pyramid 

     
#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *

def diamondStarPattern(n: int):
    for i in range(n):
        print(" " * (n-i), end="")

        print("*" * (2 * i - 1))
    
    for j in range(n):
        print(" " * j, end="")

        print("*" * (n-j), end="")

        print("*" * (n-j-1))

print(f"\n Diamond Star Pyramid \n")
print(diamondStarPattern(5))


# Pattern - 10: Half Diamond Star Pattern

# Problem Statement: Given an integer N, print the following pattern : 5
# Input Format: N = 3
# Result: 
#   *  
#   **
#   ***  
#   **
#   * 


def HaifDiamondStarPattern(n : int):
    for i in range(n):
        print("*" * i)

    for j in range(n):
        print("*" * (n-j))


print(f"\n Half Diamond Star Pyramid \n")
print(HaifDiamondStarPattern(5))


# Pattern - 11: Binary Number Triangle Pattern

# Problem Statement: Given an integer N, print the following pattern : 5

# Input Format: N = 3

# Result: 

# 1  
# 0  1  
# 1  0  1  
# 0  1  0  1  
# 1  0  1  0  1  

def PrintBinaryPattern(n : int):
    for i in range(n):
        if i % 2 == 0:
            val = 1
        else:
            val = 0
        
        for j in range(i+1):
            print(val, " ", end="")
            val = 1 - val
        print()

print(f" \n Binary Pattern \n")
print(PrintBinaryPattern(5))


# Pattern - 12: Number Crown Pattern

# Problem Statement: Given an integer N, print the following pattern : 5

# 1  
# 1  2  
# 1  2  3  
# 1  2  3  4 

def NumberCrownPattern(n: int):
    for i in range(n):
        for j in range(i):
            print(j+1, " ", end="")
        print()
       

print(f" \n Number Crown Pattern \n")
print(NumberCrownPattern(5))


# Pattern - 12 - b: Number Crown Pattern

# Problem Statement: Given an integer N, print the following pattern : 5

# 1                1
# 1  2           2 1
# 1  2  3      3 2 1
# 1  2  3  4 4 3 2 1 

