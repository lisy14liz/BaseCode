import random


def partition(arr, low, high):
    # random version
    random_idx = random.randint(low, high)
    arr[random_idx], arr[high] = arr[high], arr[random_idx]

    x = arr[high]
    i = low-1 # (elements in [low,i]) <= x
    for j in range(low, high):
        if arr[j] <= x:  # here <= to keep stability, but with random the algorithm is not stable.
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1] # 这一句相当于循环内部的两句
    return i+1


def quickSort(arr, low=None, high=None): # arr[low:high+1]
    if low is None:
        low = 0
    if high is None:
        high = len(arr)-1
    if low < high:
        q = partition(arr, low, high)
        quickSort(arr, low, q-1)
        quickSort(arr, q+1, high)


def mergeArray(arr1, arr2):
    res = []
    idx1 = idx2 = 0
    while idx1 < len(arr1) and idx2 < len(arr2):
        if arr1[idx1] <= arr2[idx2]:
            res.append(arr1[idx1])
            idx1 += 1
        else:
            res.append(arr2[idx2])
            idx2 += 1
    res = res+arr1[idx1:] if idx1 < len(arr1) else res+arr2[idx2:]
    return res


def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = mergeSort(arr[0:mid])
    right = mergeSort(arr[mid:])
    return mergeArray(left, right)
