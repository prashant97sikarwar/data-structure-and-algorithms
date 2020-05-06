def toh(n,fr,to,ax):
    if n == 1:
        print('move disk 1 from rod ' + str(fr) + ' to rod ' + str(to))
        return
    toh(n-1,fr,ax,to)
    print('move disk ' + str(n) +' from rod ' + str(fr) + ' to rod ' + str(to))
    toh(n-1,ax,to,fr)
t = int(input())
while t > 0:
    n = int(input())
    toh(n,1,3,2)
    print(2**n - 1)
    t -= 1
    