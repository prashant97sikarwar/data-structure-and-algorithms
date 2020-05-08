def insertionSort(arr): 
    for i in range(1, len(arr)): 
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j] : 
                arr[j + 1] = arr[j] 
                j -= 1
        arr[j + 1] = key 

t = int(input())
while t > 0:
    n = int(input())
    arr = list(map(int,input().split()))
    print(insertionSort(arr))
    t -= 1