from collections import defaultdict

def countDistinct(arr, N, K):
    mp = defaultdict(lambda: 0)
    res = []
    count = 0
    for i in range(K):
        if mp[arr[i]] == 0:
            count += 1
        mp[arr[i]] += 1
    
    res.append(count)
    
    for i in range(K,N):
        if mp[arr[i-K]] == 1:
            count -= 1
        mp[arr[i-k]] -= 1
        if mp[arr[i]] == 0:
            count += 1
        mp[arr[i]] += 1
        res.append(count)
    return res

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n,k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        res = countDistinct(arr, n, k)
        for i in res:
            print (i, end = " ")
        print ()