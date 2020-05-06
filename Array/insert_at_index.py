def insertAtIndex( arr, sizeOfArray, index, element):
    for i in range(sizeOfArray-1,index,-1):
        arr[i] = arr[i-1]
    arr[index] = element
    return
