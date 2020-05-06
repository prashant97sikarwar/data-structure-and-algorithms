def poww(N,R):
    
    if R == 0:
        return 1
    elif R == 1:
        return N % 1000000007
    else:
        sqrt = poww(N,R//2) % 1000000007
        return sqrt**2 * poww(N,R % 2) % 1000000007

T = int(input())

for i in range(T):
    st = input()
    N = int(st)
    R = int(st[::-1])
    print(poww(N,R))