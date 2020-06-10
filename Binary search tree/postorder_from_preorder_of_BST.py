  
INT_MIN = -2**31
INT_MAX = 2**31
  
 
def findPostOrderUtil(pre, n, minval,  
                      maxval, preIndex): 
 
    if (preIndex[0] == n): 
        return
   
    if (pre[preIndex[0] ] < minval or 
        pre[preIndex[0] ] > maxval): 
        return

    val = pre[preIndex[0]]  
    preIndex[0] += 1
  
    findPostOrderUtil(pre, n, minval, 
                       val, preIndex)  
  
 
    findPostOrderUtil(pre, n, val,  
                      maxval, preIndex)  
  
    print(val, end = " ") 
  
def findPostOrder(pre, n):  
 
    preIndex = [0]  
  
    findPostOrderUtil(pre, n, INT_MIN,  
                    INT_MAX, preIndex) 
t = int(input())
while t > 0:
    n = int(input())
    pre = list(map(int,input().split()))
    findPostOrder(pre, n) 
    print()
    t -= 1
    