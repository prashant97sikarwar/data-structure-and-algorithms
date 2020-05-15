def XNOR(i, j):
    a = A[i]
    b = A[j]
    aa = (2 ** 30 - 1) & ~a
    bb = (2 ** 30 - 1) & ~b
    return (a & b) | (aa & bb)
 
def solve(A):
    n_dict = dict([(i + 1, A[i]) for i in range(len(A))])
    n_dict_ord = sorted(n_dict.items(), key = lambda kv:(kv[1], kv[0]))
    min_i = len(A)
    max_xnor = 0
    min_j = len(A)
    for i in range(1, len(A)):
        c_xnor = XNOR(n_dict_ord[i][0] - 1, n_dict_ord[i - 1][0] - 1) - 2 ** 30
        if c_xnor > max_xnor:
            max_xnor = c_xnor
            min_i = min(n_dict_ord[i - 1][0], n_dict_ord[i][0])
            min_j = max(n_dict_ord[i - 1][0], n_dict_ord[i][0])
        else:
            if c_xnor == max_xnor:
                min_i = min(min(min_i, n_dict_ord[i - 1][0]), n_dict_ord[i][0])
    z = 0
    
    c_xnor = 0
    
    while A[z] != A[min_i - 1]:
        z += 1
    min_i = z + 1
    
    z = 0
    while z < len(A):
        if z != min_i - 1:
            tmp = XNOR(min_i - 1, z)
            if tmp > c_xnor:
                c_xnor = tmp
                min_j = z
        z += 1
        
    min_j += 1
    return min_i, min_j
    
T = int(input())
 
for _ in range(T):
    n = int(input())
    A = list(map(lambda s: int(s) + 2 ** 30, input().split()))
    print(*solve(A))