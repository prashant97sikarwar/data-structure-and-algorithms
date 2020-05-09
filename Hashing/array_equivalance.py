import collections
t = int(input())
while t > 0:
    n = int(input())
    arr = list(map(int,input().split()))
    brr = list(map(int,input().split()))
    if collections.Counter(arr) == collections.Counter(brr):
        print(1)
    else:
        print(0)
    
    t -= 1