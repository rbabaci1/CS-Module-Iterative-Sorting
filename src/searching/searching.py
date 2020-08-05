def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # found
    return -1  # not found


def binary_search(arr, target):
    start, end = 0, len(arr) - 1
    while start <= end:
        midpoint = start + end // 2
        if arr[midpoint] == target:
            return midpoint  # found
        if arr[midpoint] > target:
            end = midpoint - 1
        else:
            start = midpoint + 1
    return -1  # not found
