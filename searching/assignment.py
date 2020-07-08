from sys import *
n = int(stdin.readline())
key = int(stdin.readline())
arr = list(map(int,stdin.readline().split()))
my_search_ds = [-1 for i in range(n)]
for i in range(n):
    index = arr[i] % n
    if my_search_ds[index] == -1:
        my_search_ds[index] = arr[i]
    else:
        for j in range(1,n):
            newindex = index + j
            if newindex >= n:
                newindex -= n
            if my_search_ds[newindex] == -1:
                my_search_ds[newindex] = arr[i]
                break

def search(my_search_ds,key,n):
    check_in = key % n
    if my_search_ds[check_in] == key:
        return check_in
    else:
        for j in range(1,n):
            another_check = check_in + j
            if another_check >= n:
                another_check -= n
            if my_search_ds[another_check] == key:
                return another_check


print(search(my_search_ds,key,n))