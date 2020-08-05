def selection_sort(arr):
    for i in range(0, len(arr) - 1):
        smallest_elem_index = i
        for j in range(i, len(arr)):
            if arr[j] < arr[smallest_elem_index]:
                smallest_elem_index = j
        if smallest_elem_index != i:
            arr[i], arr[smallest_elem_index] = arr[smallest_elem_index], arr[i]
    return arr


def bubble_sort(arr):
    for i in range(0, len(arr) - 1):
        flag = 1
        for j in range(0, len(arr) - (i + 1)):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                flag = 0
        if flag:
            break
    return arr


a = [26, 5, 7, 3, 1]
print(bubble_sort(a))

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
    # Your code here

    return arr
