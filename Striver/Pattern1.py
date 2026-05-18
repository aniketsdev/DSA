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


