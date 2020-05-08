def yo(arr,l,h,n):
    if h >= l:
        mid = l + (h-l)//2
        if arr[mid] > arr[0] and arr[mid] < arr[n-1]:
            return arr[0]
        else:
            if arr[mid] < arr[mid-1] or n == 1:
                return arr[mid]
            elif (arr[mid] > arr[mid-1]) and (arr[mid] > arr[0]):
                return yo(arr,mid+1,h,n)
            else:
                return yo(arr,l,mid-1,n)
        
        
t = int(input())
while t > 0:
    n = int(input())
    arr = list(input().split())
    for i in range(n):
        arr[i] = int(arr[i])
    print(yo(arr,0,n-1,n))
    t -= 1