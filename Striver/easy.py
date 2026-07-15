# Find the Largest element in an array

# Problem Statement: Given an array, we have to find the largest element in the array.

# Example 1:
# Input: arr[] = {2, 5, 1, 3, 0}  
# Output: 5  

# Explanation:
# 5 is the largest element in the array.

# Example 2:
# Input: arr[] = {8, 10, 5, 7, 9}  
# Output: 10  
# Explanation:
# 10 is the largest element in the array.

def largest(arr):
    n = len(arr)
    LargestElement = 0
    for i in range(n):
        # print(arr[i] , arr[i-1])
        if arr[i] >= arr[i-1] and arr[i] >= LargestElement:
            # print(arr[i])
            LargestElement = arr[i]
            # print(LargestElement)
    
    return LargestElement

arr = [8, 10, 5, 19, 9]
print("\n Largest Element\n")
print(largest(arr))