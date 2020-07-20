arr = [1,2]
while arr[-1] < 4000000:
    dep = arr[-1] + arr[-2]
    if dep <= 4000000:
        arr.append(dep)
    else:
        break

ans = 0
for i in range(len(arr)):
    if arr[i] % 2 == 0:
        ans += arr[i]
print(ans)