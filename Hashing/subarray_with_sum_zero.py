def sumExists(arr,n):
    s = set()
    sum = 0
    for i in range(n):
        sum += arr[i]
        if sum == 0 or sum in s:
            return 'Yes'
        s.add(sum)
    return 'No'
t = int(input())
while t > 0:
    n = int(input())
    arr = list(map(int,input().split()))
    print(sumExists(arr,n))
    t -= 1