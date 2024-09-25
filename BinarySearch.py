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



x = [1,1]
target_value = 5

def binarySearchIdxLower(arr, low, high, target, idx):
    if high >= low:
        mid = (high + low) // 2
        print(str(arr[mid]) + " this is from lower")
        if arr[mid] == target:
            if (idx == -1 or mid < idx):
                idx = mid
        if arr[mid] >= target:
            return binarySearchIdxLower(arr, low, mid - 1, target, idx)
        else:
            return binarySearchIdxLower(arr, mid + 1, high, target, idx)
    else:
        return idx
    
def binarySearchIdxUpper(arr, low, high, target, idx):
    if high >= low:
        mid = (high + low) // 2
        print(str(mid) + " this is from upper")
        if arr[mid] == target:
            if (mid > idx):
                idx = mid
        if arr[mid] > target:
            return binarySearchIdxUpper(arr, low, mid - 1, target, idx)
        else:
            return binarySearchIdxUpper(arr, mid + 1, high, target, idx)
    else:
        return idx
    
    
print(binarySearchIdxLower(x, 0, len(x)-1, target_value, -1))
print(binarySearchIdxUpper(x, 0, len(x)-1, target_value, -1))