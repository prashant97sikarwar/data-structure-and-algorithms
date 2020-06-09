import math
def fun(root,min_diff,k):
    if root is None:
        return 
    if root.data == k:
        min_diff[0] = 0
        return
    if min_diff[0] > abs(root.data - k):
        min_diff[0] = abs(root.data - k)
        
    if k > root.data:
        fun(root.right,min_diff,k)
    if k < root.data:
        fun(root.left,min_diff,k)
        

def minDiff(root, K):
    min_diff = [math.inf]
    fun(root,min_diff,k)
    return min_diff[0]

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
        print(minDiff(root,K))
        