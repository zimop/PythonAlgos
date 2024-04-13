def binarySearch(arr, low, high, target):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return binarySearch(arr, low, mid - 1, target)
        else:
            return binarySearch(arr, mid + 1, high, target)
    else:
        return -1

arr = [2, 3, 4, 10, 40]
x = 10

result = binarySearch(arr, 0, len(arr)-1, x)