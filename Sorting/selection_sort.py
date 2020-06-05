def select_sort(arr,n):
    for i in range(n):
        min_in = i
        for j in range(i+1,n):
            if arr[j] < arr[min_in]:
                min_in = j
        arr[i],arr[min_in] = arr[min_in],arr[i]
        

n = int(input())
arr = list(map(int,input().split()))
select_sort(arr,n)
print(arr)