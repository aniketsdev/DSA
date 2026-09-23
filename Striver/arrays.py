# Given an array of integers nums and an integer target, find the smallest index (0 based indexing) where the target appears in the array. If the target is not found in the array, return -1
# Example 1:
# Input: nums = [2, 3, 4, 5, 3], target = 3

# Output: 1

# Explanation:

# The first occurence of 3 in nums is at index 1

# Example 2:
# Input: nums = [2, -4, 4, 0, 10], target = 6

# Output: -1

# Explanation:

# The value 6 does not occur in the array, hence output is -1
# Using linear search

# def linearSearch(arr, target):
#     n = len(arr)
#     for i in range(n):
#         if arr[i] == target:
#             return i

#     return -1

# Using binary search

def linearSearch(arr, target):
    left = 0
    right = len(arr) - 1
    answer = -1

    while left <= right:
        # print("test")
        mid = left + (right - left) // 2

        if arr[mid] == target:
            # print(answer)
            answer = mid
            right = mid - 1

        elif arr[mid] < target:
            # print(arr[mid])
            left = mid + 1

        else:
            # print("demo")
            right = mid - 1

    return answer



arr1 = [2, 7, 10 , 33, 83]
tar = 7
print("Target Element Index is : ")
print(linearSearch(arr1, tar))

# 702. Largest Element

# Given an array of integers nums, return the value of the largest element in the array

# Example 1:
# Input: nums = [3, 3, 6, 1]

# Output: 6

# Explanation: The largest element in array is 6

# Example 2:
# Input: nums = [3, 3, 0, 99, -40]

# Output: 99

# Explanation: The largest element in array is 

def largestElement(nums):
    n = len(nums)
    largest = -1

    for i in range(n):
        if arr[i] > arr[i-1] and arr[i] >= largest:
            largest = arr[i]

    return largest

arr = [2, 54, 87, 3, 6, 99]
print("Largest Element in Array")
print(largestElement(arr))

