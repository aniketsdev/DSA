def RemoveDuplicate(arr: list) -> list:
    n = len(arr)

    arr.sort()
    unique_arr = []
    for j in range(n):
        if arr[j] != arr[j-1]:
            unique_arr.append(arr[j])
    
    return unique_arr


def PrintDuplicate(arr: list) -> list:
    n = len(arr)
    arr.sort()
    duplicate_arr = []

    for i in range(n):
        if arr[i] == arr[i-1]:
            duplicate_arr.append(arr[i])
    
    return duplicate_arr



my_list = [3, 56, 13 , 11 , 13, 78, 43, 56]
print(f" Unique Valies : {RemoveDuplicate(my_list)} , Duplicate Values : {PrintDuplicate(my_list)}")