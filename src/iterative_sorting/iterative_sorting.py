def selection_sort(arr):
    for i in range(len(arr) - 1):
        smallest_elem_index = i
        for j in range(i, len(arr)):
            if arr[j] < arr[smallest_elem_index]:
                smallest_elem_index = j
        if smallest_elem_index != i:
            arr[i], arr[smallest_elem_index] = arr[smallest_elem_index], arr[i]
    return arr


def bubble_sort(arr, opt=1):
    for i in range(len(arr) - 1):
        swap_occurred = False
        for j in range(len(arr) - (i + 1)):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap_occurred = True
        if not swap_occurred:
            break
    return arr


# def recursive_bubble_sort(arr, opt=1):
#     unsorted_len = len(arr)
#     swap_occurred = False
#     for j in range(unsorted_len - opt):
#         if arr[j] > arr[j + 1]:
#             arr[j], arr[j + 1] = arr[j + 1], arr[j]
#             swap_occurred = True

#     if not swap_occurred or not unsorted_len:
#         return arr
#     else:
#         bubble_sort(arr, opt + 1)

#     return arr


"""
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
"""


def counting_sort(arr, maximum=None):
    sortedArr = [0 for n in arr]  # O(n)
    if len(arr):
        if not maximum:
            maximum = arr[0]
            for i in range(len(arr)):  # O(n)
                if arr[i] < 0:
                    return "Error, negative numbers not allowed in Count Sort"
                if arr[i] > maximum:
                    maximum = arr[i]

        counterArr = [0 for i in range(maximum + 1)]  # O(k) where k is the max in arr

        for num in arr:  # O(n)
            counterArr[num] += 1
        for i in range(1, len(counterArr)):  # O(k) where k is the max number in arr
            counterArr[i] = counterArr[i - 1] + counterArr[i]

        end = len(arr) - 1
        while end >= 0:  # O(n)
            current = arr[end]
            index = counterArr[current] - 1
            sortedArr[index] = current
            end -= 1
    return sortedArr

    """
    1- The time complexity for this algorithm is O(n + k)
    2- The space complexity is O(n + k) where k is the maximum number in the array
    """
