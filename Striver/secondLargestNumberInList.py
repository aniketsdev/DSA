# Print second Largest Number in array

# One pass approach
def secondLargestNumber(arr: list) -> list:
    n = len(arr)
    Largest = -1
    secondLargest = -1
    for i in range(n):
        if arr[i] > Largest:
            secondLargest = Largest
            Largest = arr[i]
    
    return secondLargest


my_list = [12, 43, 23, 87, 11, 34]
print(secondLargestNumber(my_list))