# Bubble Sort
# sort = [12, 11, 87, 45, 23, 98, 59]

def Sorted_arr(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j] , arr[j+1] = arr[j+1], arr[j]
    return arr

my_arr = [17, 2, 54, 23, 98, 43, 56]
print(Sorted_arr(my_arr))




# def Sorted_arr(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(0, n-i-1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
    
#     return arr

# my_arr = [12, 11, 87, 45, 23, 98, 59]
# print(f"\n Sort the Array")
# print(Sorted_arr(my_arr))




# Selection Sort

def selectionSort(arr: list):
    n = len(arr)

    for boundry in range(n-1):
        min_length = boundry

        for current in range(boundry+1, n):
            if arr[current] < arr[min_length]:
                min_length = current

        if arr[min_length] != arr[boundry]:
            arr[min_length], arr[boundry] = arr[boundry] , arr[min_length]

    return arr

    

    # n = len(arr)

    # for i in range(n):
    #     min_index = i
    #     for j in range(i+1, n):
    #         if arr[j] < arr[min_index]:
    #             min_index = j

    #     arr[i] , arr[min_index] = arr[min_index], arr[i]
    
    # return arr

arr = [13, 46, 24, 52, 20, 9]
print(f"/n Selection Sort Algorithm ")
print(selectionSort(arr))

# Pass 1:
# 13 46 24 52 20 9
# ↓
# 9 46 24 52 20 13

# Pass 2:
# 9 46 24 52 20 13
# ↓
# 9 13 24 52 20 46

# Pass 3:
# 9 13 24 52 20 46
# ↓
# 9 13 20 52 24 46

# Pass 4:
# 9 13 20 52 24 46
# ↓
# 9 13 20 24 52 46

# Pass 5:
# 9 13 20 24 52 46
# ↓
# 9 13 20 24 46 52


# Bubble sort
def bubbleSort(arr: list):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j] , arr[j+1] = arr[j+1], arr[j]

        
    return arr

arr = [13, 46, 24, 52, 20, 9]
print(f"/n Bubble Sort Algorithm ")
print(bubbleSort(arr))


# Optimized bubble sort ay
def optimizedBubbleSort(arr: list):
    n = len(arr)

    for i in range(n):
        swap = False

        for j in range(0, n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j] , arr[j+1] = arr[j+1], arr[j]
                swap = True
        
        if not swap:
            break

    return arr

arr = [13, 46, 24, 52, 20, 9]
print(f"/n Optimized Bubble Sort Algorithm ")
print(optimizedBubbleSort(arr))




# Insertion sort
def insertionSort(arr: list):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        
        arr[j+1] = key
    
    return arr

arr = [13, 46, 24, 52, 20, 9]
print(f"/n Insertion Sort Algorithm ")
print(insertionSort(arr))


# Merge Sort
# Think of Merge Sort as two separate problems:

# Split the array until only one element remains.
# Merge those single elements back in sorted order.

# That's all Merge Sort does.
class Solution:
    def merge(self, arr, low, mid, high):
        temp = []
        left, right = low , mid  + 1

        while left <= mid and right <= high:
            # print("----------------", left <= mid, right >= high)
            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left+=1
            else:
                temp.append(arr[right])
                right+=1
        
        while left <= mid:
            temp.append(arr[left])
            left+=1
        
        while right <= high:
            temp.append(arr[right])
            right+=1
        
        for i in range(low, high+1):
            arr[i] = temp[i - low]

    def mergeSort(self, arr, low, high):
        if low >= high:
            return
        mid = (low + high) // 2
        self.mergeSort(arr, low, mid)
        self.mergeSort(arr, mid + 1, high)
        self.merge(arr, low , mid, high)    


arr_two = [3, 9, 1, 4, 7, 2]
print("\n Merge Sort : \n")
sol = Solution()
sol.mergeSort(arr_two, 0, len(arr_two)-1)
print(*arr_two)