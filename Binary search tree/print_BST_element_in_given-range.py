def fun(root,low,high,l):
    if root is None:
        return 
    if low < root.data:
        fun(root.left,low,high,l)
    if low <= root.data and high >= root.data:
        l.append(root.data)
    if high > root.data:
        fun(root.right,low,high,l)
    return l

def printNearNodes(root, low, high):
    l = []
    des = fun(root,low,high,l)
    return des
    
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
        n1,n2=list(map(int,input().split()))
        res = printNearNodes(root,n1,n2);
        for i in range (len(res)):
            print (res[i], end = " ")
        print()