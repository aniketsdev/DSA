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
       if arr[i] >= arr[i-1] and arr[i] >= LargestElement:
           LargestElement = arr[i]

    return LargestElement

arr = [8, 60, 5, 19, 9]
print("\n Largest Element\n")
print(largest(arr))


# Find Second Smallest and Second Largest Element in an array

# Problem Statement: Given an array, find the second smallest and second largest element in the array. Print ‘-1’ in the event that either of them doesn’t exist.

# Example 1:
# Input:
#  [1, 2, 4, 7, 7, 5]  
# Output:
  
# Second Smallest : 2  
# Second Largest : 5  
# Explanation:
#   The elements are sorted as 1, 2, 4, 5, 7, 7.  
# Hence, the second smallest element is 2, and the second largest element is 5.

# Example 2:
# Input:
#  [1]  
# Output:
  
# Second Smallest : -1  
# Second Largest : -1  
def SecondLargestNumber(arr: list):
    # n = len(arr)

    # arr.sort()
    # largest = 0
    # SecondLargestNumber = 0

    # for i in range(n):
    #     if arr[i] >= arr[i-1] and arr[i] >= largest and arr[i] != arr[i-1]:
    #         SecondLargestNumber = largest
    #         largest = arr[i]

    # return SecondLargestNumber
    

    n = len(arr)

    if n <= 1:
        return -1

    largestElement , secondLargestElement = 0 , 0
    arr.sort()
    for i in range(n):
        # print(arr[i])
        if arr[i] > arr[i-1] and largestElement < arr[i]:
            # print(secondLargestElement, largestElement)
            secondLargestElement = largestElement
            largestElement = arr[i]

    return secondLargestElement

# Optimal solution


arr = [1, 2, 4, 6, 6, 5] 
print("\n Second largest Number \n")
print(SecondLargestNumber(arr))

# Check if an Array is Sorted

# Problem Statement: Given an array of size n, write a program to check if the given array is sorted in (ascending / Increasing / Non-decreasing) order or not. If the array is sorted then return True, Else return False.

def checkSortedArray(arr: list):
    n = len(arr)
    if n <= 1:
        return True

    # for i in range(n):
    #     for j in range(i+1, n):
    #         if arr[j] <= arr[i]:
    #             return False
    
    for i in range(1, n):
        if arr[i] < arr[i-1]:
            return False

    return True

arr = [1, 2, 3, 8, 10]
print("\n Check sorted Array \n ")
print(checkSortedArray(arr))


# Remove Duplicates in-place from Sorted Array

# Problem Statement: Given an integer array sorted in non-decreasing order, remove the duplicates in place such that each unique element appears only once. The relative order of the elements should be kept the same.
# If there are k elements after removing the duplicates, then the first k elements of the array should hold the final result. It doesn't matter what you leave beyond the first k elements.

def removeDuplicatesIn(arr: list):
    arr = 


arr = [1, 1, 3, 3, 10, 34]
print("\n Remove Duplicates in-place from Sorted Array \n ")
print(removeDuplicatesIn(arr))

    