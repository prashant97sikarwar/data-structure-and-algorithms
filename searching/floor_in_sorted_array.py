def binary(arr,l,h,x):
    if h ==l:
        if arr[l] <= x:
            return l
    elif h>l:
        mid = l + (h-l)//2
        if arr[mid] > x:
            return binary(arr,l,mid-1,x)
        elif arr[mid] <= x and arr[mid+1] > x:
            return mid
        else:
            return binary(arr,mid+1,n-1,x)
t = int(input())
while t > 0:
    n,x = map(int,input().split())
    arr = list(map(int,input().split()))
    l = 0
    h = n-1
    index = (binary(arr,l,h,x))
    if(index):
        print(index)
    else:
        print(-1)
    t -= 1
    