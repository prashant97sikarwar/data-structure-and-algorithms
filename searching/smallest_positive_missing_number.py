def segregate(arr,n):
    j = 0
    for i in range(n):
        if arr[i] <= 0:
            arr[i],arr[j] = arr[j],arr[i]
            j += 1
    return j

def find(arr,size):
    for i in range(size):
        if abs(arr[i]) -1 < size and arr[abs(arr[i])-1] > 0:
            arr[abs(arr[i])-1] = -arr[abs(arr[i])-1]
    for i in range(size):
        if arr[i] > 0:
            return i + 1
    return size + 1
    
def func(arr,n):
    l = segregate(arr,n)
    ans = find(arr[l:],n - l)
    return ans
t = int(input())
while t > 0:
    n = int(input())
    arr = list(input().split())
    for i in range(n):
        arr[i] = int(arr[i])
    yo = func(arr,n)
    print(yo)
    t -= 1
    