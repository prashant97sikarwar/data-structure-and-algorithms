t = int(input())
while t > 0:
    n = int(input())
    arr = input()
    count = 0
    for i in range(n):
        if arr[i] == '1':
            count += 1
    ans = (count * (count - 1))//2
    print(ans)
    t -= 1