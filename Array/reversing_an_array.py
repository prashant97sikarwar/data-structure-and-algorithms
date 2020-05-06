def arrayReversal(arr,sizeOfArr):
    l = 0
    r = sizeOfArr - 1
    while l < r:
        arr[l],arr[r] = arr[r],arr[l]
        l += 1
        r -= 1
    return