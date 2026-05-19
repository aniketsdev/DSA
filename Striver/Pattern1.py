# Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:

# *****
# *****
# *****
# *****
# *****

def Pattern(n):
    for i in range(n):
        for j in range(n):
            print("*", end="")
        print()


print(Pattern(5))


# Pattern-2: Right-Angled Triangle Pattern

# Problem Statement: Given an integer N, print the following pattern 

# *
# * *
# * * *
# * * * *
# * * * * *

def RightAngleTrianglePattern(n):
    for i in range(n):
        for j in range(i):
            print("* ", end = '')
        print()

print("Right Angle Triangle")
print(RightAngleTrianglePattern(5))


# Pattern - 3: Right-Angled Number Pyramid

# Problem Statement: Given an integer N, print the following pattern : 

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

def NumberedPattern(n):
    for i in range(n):
        for j in range(i):
            print(j+1, " ", end="")
        print()

print("Numbered Pattern")
print(NumberedPattern(6))


# Pattern - 4: Right-Angled Number Pyramid - II

# Problem Statement: Given an integer N, print the following pattern : 

# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

def NumberedPatternTwo(n):
    for i in range(n):
        for j in range(i):
            print(i, " ", end="" )
        print()

print(NumberedPatternTwo(6))


# Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:

# *****
# ****
# ***
# **
# *


def ReversePattern(n):
    for i in range(n):
        for j in range(n-i):
            print("*", end="")
        print()

print("Reversed Pattern")
print(f"{ReversePattern(5)}")

