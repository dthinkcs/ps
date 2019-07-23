def quickSort(arr):
    # Write your code here.
    if len(arr) <= 1:
        return arr
    else:
        pivot = findPivotAndPartition(arr)
        leftSorted = quickSort(arr[:pivot])
        rightSorted = quickSort(arr[pivot + 1:])
        return leftSorted + [ arr[pivot] ] + rightSorted

def findPivotAndPartition(arr):
    pivot = 0
    for i in range(1, len(arr)):
        if arr[i] < arr[0]:
            pivot += 1

    arr[pivot], arr[0] = arr[0], arr[pivot]

    i = 0
    j = len(arr) - 1
    while True:
        if i >= pivot or j <= pivot:
            break
        if arr[i] >= arr[pivot] and arr[j] < arr[pivot] :
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
        elif arr[i] >= arr[pivot]:
            j -= 1 # BUG: if i is wrong and  j is correct then decrement j NOT I
        else:
            i += 1
    return pivot
