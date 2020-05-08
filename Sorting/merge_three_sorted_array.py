def merge_two(a, b): 
    (m, n) = (len(a), len(b)) 
    i = j = 0
    d = [] 
    while i < m and j < n: 
        if a[i] <= b[j]: 
            d.append(a[i]) 
            i += 1
        else: 
            d.append(b[j]) 
            j += 1
    while i < m: 
        d.append(a[i]) 
        i += 1
    while j < n: 
        d.append(b[j]) 
        j += 1
  
    return d
  
def merge(a, b, c): 
    t = merge_two(a, b) 
    return merge_two(t, c) 
t = int(input())
while t > 0:
    m,n,o = map(int,input().split())
    arr1 = list(map(int,input().split()))
    arr2 = list(map(int,input().split()))
    arr3 = list(map(int,input().split()))
    ans = merge(arr1, arr2, arr3)
    for i in range(len(ans)):
        print(ans[i],end=' ')
    print()
    t -= 1