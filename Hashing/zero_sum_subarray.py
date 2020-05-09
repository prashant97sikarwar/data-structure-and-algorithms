from collections import defaultdict 

def findSubarraySum(arr, n):  
    prevSum = defaultdict(lambda : 0) 
    
    res = 0 
    currsum = 0 
    
    for i in range(0, n):   
      
        currsum += arr[i]  
        if currsum == 0:   
            res += 1         
        if (currsum - 0) in prevSum: 
            res += prevSum[currsum - 0]  
        prevSum[currsum] += 1 
       
    return res  
t = int(input())
while t > 0:
    n = int(input())
    arr = list(map(int,input().split()))
    print(findSubarraySum(arr,n))
    t -= 1