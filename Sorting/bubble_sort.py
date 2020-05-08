def bubbleSort(arr,n):
    for i in range(n):
        swapped = True
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swapped = True
        if swapped == False:
            break
    return arr

t = int(input())
while t > 0:
    n = int(input())
    arr = list(map(int,input().split()))
    print(bubbleSort(arr,n))
    t -= 1