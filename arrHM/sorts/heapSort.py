# 2 BUGS: 1.ci, pi = pi, (ci - 1) // 2 (II.) len - 2 - i
def heapSort(arr):
    # create a max heap
    for i in range(len(arr)):
        # inserted now up heapify
        ci = i
        pi = (i - 1) // 2
        while True:
            if pi < 0:
                break
            elif arr[pi] > arr[ci]:
                break
            else:
                arr[pi], arr[ci] = arr[ci], arr[pi]

            # we DONT Want want that here ci, pi = pi, (ci - 1) // 2
            ci = pi
            pi = (ci - 1) // 2

    # take out from the top and put it behind
    for i in range(len(arr)):
        arr[0], arr[len(arr) - 1 - i] = arr[len(arr) - 1 - i], arr[0]
        # downheapify
        pi = 0
        li = 2 * pi + 1
        ri = 2 * pi + 2
        while True:
            if pi >= len(arr) - 1 - i -1:
                break
            maxIdx = pi
            if li <= len(arr) - 1 - i - 1 and arr[li] > arr[maxIdx]:
                maxIdx = li
            if ri <= len(arr) - 1 - i - 1 and arr[ri] > arr[maxIdx]:
                maxIdx = ri

            if pi == maxIdx:
                break
            arr[maxIdx], arr[pi] = arr[pi], arr[maxIdx]
            pi = maxIdx
            li = 2 * pi + 1
            ri = 2 * pi + 2

    return arr
