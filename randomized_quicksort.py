import random

def randomized_quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]
    less = [x for i, x in enumerate(arr) if x < pivot and i != pivot_index]
    equal = [x for x in arr if x == pivot]
    greater = [x for i, x in enumerate(arr) if x > pivot and i != pivot_index]
    return randomized_quicksort(less) + equal + randomized_quicksort(greater)
