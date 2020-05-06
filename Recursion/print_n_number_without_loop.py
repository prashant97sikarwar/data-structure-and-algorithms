def num(n):
    if n > 0:
        num(n-1)
        print(n,end=' ')
t = int(input())
while t > 0:
    n = int(input())
    num(n)
    print()
    t-=1