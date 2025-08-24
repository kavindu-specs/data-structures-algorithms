import time

arr = [64,23,56,33,12,67,89,34]

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(0,len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1], arr[j]
        #print(arr)
    return arr

def insertion_sort(arr):
    for i in range(1,len((arr))):
        key = arr[i]
        j = i-1
        while j>=0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
            arr[j+1] = key
    return arr
    
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        #print("left--",left)
        #print("right--",right)
        merge_sort(left)
        merge_sort(right)
        
        i = j = k =0

        while i < len(left) and j < len(right):
            if left[i] <  right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        #print("sorted--",arr)

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        #print("sorted1--",arr)

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
        #print("sorted2--",arr)
    return arr

def tim_sort(arr):
    RUN = 2
    for i in range(0,len(arr),RUN):
        insertion_sort(arr[i:i+RUN])
    
    

if __name__ == "__main__":
    arr1 = arr.copy()
    arr2 = arr.copy()
    arr3 = arr.copy()

    start = time.time()
    print("Bubble Sort Result:", bubble_sort(arr1))
    print("Bubble Sort Time: {:.6f} seconds".format(time.time() - start))

    start = time.time()
    print("Insertion Sort Result:", insertion_sort(arr2))
    print("Insertion Sort Time: {:.6f} seconds".format(time.time() - start))

    start = time.time()
    print("Merge Sort Result:", merge_sort(arr3))
    print("Merge Sort Time: {:.6f} seconds".format(time.time() - start))