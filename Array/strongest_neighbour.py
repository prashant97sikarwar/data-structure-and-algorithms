def maximumAdjacent(sizeOfArray, arr):
    for i in range(sizeOfArray-1):
        l = max(arr[i],arr[i+1])
        print(l,end=' ')
    return 