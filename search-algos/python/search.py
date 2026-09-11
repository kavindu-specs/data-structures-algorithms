import time

arr = [64,23,56,33,12,67,89,34]
sorted_array = [12,23,33,34,56,64,67,89]

def linear_search(arr,target):
    for i,num in enumerate(arr):
        if num == target:
            return i
    return -1

def binary_search(arr,target):
    if len(arr) == 0:
        return -1  # Not found
    middle_index = len(arr)//2
    if arr[middle_index] == target:
        return middle_index
    elif arr[middle_index] < target:
        return binary_search(arr[middle_index+1:],target)
    else:
        return binary_search(arr[:middle_index],target)

def jump_search(arr, target):
    import math
    n = len(arr)
    step = int(math.sqrt(n))  # Optimal jump size
    prev = 0

    while prev < n and arr[min(step, n)-1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

    for i in range(prev, min(step, n)):
        if arr[i] == target:
            return i
    return -1

if __name__ == "__main__":
    arr1 = arr.copy()
    arr2 = arr.copy()
    arr3 = arr.copy()

    sorted_arr1 = sorted_array.copy()
    sorted_arr2 = sorted_array.copy()

    start = time.time()
    print("Linear Search", linear_search(arr,23))
    print("Linear Search: {:.6f} seconds".format(time.time() - start))

    start = time.time()
    print("Binary Search", binary_search(sorted_arr1,563))
    print("Binary Search: {:.6f} seconds".format(time.time() - start))

    start = time.time()
    print("Jump Search", jump_search(sorted_arr1,33))
    print("Jump Search: {:.6f} seconds".format(time.time() - start))
