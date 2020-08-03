def solve(a,b,c):
    for i in range(int(c/a)+1):
        for j in range(int(c/b) +1):
            if i*a + j*b == c:
                return True
    return False
a,b,c = map(int,input().split())
if solve(a,b,c):
    print("Yes")
else:
    print("No")