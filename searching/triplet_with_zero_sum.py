def findTriplets(a,n):
    for i in range(0,n-1): 
        s = set() 
        cu = 0 - a[i] 
        for j in range(i + 1,n): 
            if (cu - a[j]) in s: 
                return 1
            s.add(a[j]) 
    return 0