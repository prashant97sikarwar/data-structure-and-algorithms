def Solve (k, arr):
    # Write code here
    summ = 0
    count = 0
    t = k
    for i in arr:
        if i >= 0:
            count += 1
            summ += i
            t = k
        else:
            if count == 0:
                return abs(sum(arr) + i)
            else:
                t -= 1
                if t < 0:
                    summ += abs(i)
                else:
                    summ += i
    return abs(summ)
     
n, k = map(int, input().split())
    
arr = map(int, input().split())
    
out_ = Solve(k, arr)
print (out_)