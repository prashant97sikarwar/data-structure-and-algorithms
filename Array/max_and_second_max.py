def largestAndSecondLargest(sizeOfArray, arr):
    max1 = -1
    max2 = -1
    for i in range(sizeOfArray):
        if arr[i] > max1:
            max2 = max1
            max1 = arr[i]
        elif arr[i] > max2 and arr[i] < max1:
            max2 = arr[i]
    if max1 == max2:
        max2 = -1