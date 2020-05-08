def first(arr, low, high, x, n) : 
    if (high >= low) : 
        mid = low + (high - low) // 2;  # (low + high)/2;  
        if ((mid == 0 or x > arr[mid-1]) and arr[mid] == x) : 
            return mid 
        if (x > arr[mid]) : 
            return first(arr, (mid + 1), high, x, n) 
        return first(arr, low, (mid -1), x, n) 
          
    return -1

def sortAccording(A1, A2, m, n) : 
    temp = [0] * m 
    visited = [0] * m 
      
    for i in range(0, m) : 
        temp[i] = A1[i] 
        visited[i] = 0
    temp.sort() 
    ind = 0    
    for i in range(0, n) : 
        f = first(temp, 0, m-1, A2[i], m) 
        if (f == -1) : 
            continue
        j = f 
        while (j<m and temp[j]== A2[i]) : 
            A1[ind] = temp[j]; 
            ind = ind + 1
            visited[j] = 1
            j = j + 1
    for i in range(0, m) : 
        if (visited[i] == 0) : 
            A1[ind] = temp[i] 
            ind = ind + 1

def printArray(arr, n) : 
    for i in range(0, n) : 
        print(arr[i], end = " ") 
    print("") 
                 
t = int(input())
while t > 0:
    m,n = map(int,input().split())
    arr = list(map(int,input().split()))
    arr1 = list(map(int,input().split()))
    sortAccording(arr,arr1, m, n) 
    printArray(arr, m) 
    t -= 1
  