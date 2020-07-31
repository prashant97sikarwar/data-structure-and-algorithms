import math
def get_ans(n, k):
    count = 0
    ans = None
    l =[]
    sq = int(math.sqrt(n))
    for i in range(1, sq+1):
        if n%i == 0:
            count += 1
            if n/i != i:
                l.append(n/i)
        if count == k:
            ans = i 
            break

    if not ans:
        if k-count > len(l):
            return -1
        else:
            return int(l[-(k-count)])
    else:
        return ans
    
if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        n, k = list(map(int, input().split()))
        print(get_ans(n, k))