def fun(root):
    if root is None:
        return 0
    
    l = fun(root.left)
    r = fun(root.right)
    
    mxsin = max(max(l,r) + root.data, root.data)
    
    mxtp = max(mxsin,  l + r + root.data)
    
    fun.res = max(fun.res, mxtp)
    return mxsin

def findMaxSum(root):
    fun.res = float('-inf')
    fun(root)
    return fun.res

from collections import deque
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
   
def buildTree(s):
    if(len(s)==0 or s[0]=="N"):           
        return None

    ip=list(map(str,s.split()))

    root=Node(int(ip[0]))                     
    size=0
    q=deque()
  
    q.append(root)                            
    size=size+1 

    i=1                                       
    while(size>0 and i<len(ip)):
 
        currNode=q[0]
        q.popleft()
        size=size-1

        currVal=ip[i]

        if(currVal!="N"):
            
  
            currNode.left=Node(int(currVal))
            
            
            q.append(currNode.left)
            size=size+1

        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        if(currVal!="N"):

            currNode.right=Node(int(currVal))

            q.append(currNode.right)
            size=size+1
        i=i+1
    return root
    
    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        root=buildTree(s)
        print(findMaxSum(root))
