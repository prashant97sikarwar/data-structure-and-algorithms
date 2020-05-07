t = int(input())
while t > 0:
    n1,m1 = map(int,input().split())
    arr1 = list(map(int,input().split()))
    n2,m2 = map(int,input().split())
    arr2 = list(map(int,input().split()))
    if n1 == n2 and m1 == m2:
        for i in range(n1*m1):
            arr1[i] = arr1[i] + arr2[i]
        for i in range(len(arr1)):
            print(arr1[i],end=' ')
        print()
    else:
        print(-1)
    t -= 1