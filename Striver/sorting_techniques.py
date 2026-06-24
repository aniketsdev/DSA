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

    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i] , arr[min_index] = arr[min_index], arr[i]
    
    return arr

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