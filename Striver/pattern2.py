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