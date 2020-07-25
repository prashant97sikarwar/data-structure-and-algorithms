def ans(path,leng):
    for i in range(leng):
        print(path[i],end=' ')
    print('#',end='')
    
def myfun(root,path,pathlen):
    if root is None:
        return
    else:
        if len(path) > pathlen:
            path[pathlen] = root.data
        else:
            path.append(root.data)
        pathlen += 1
        if root.left is None and root.right is None:
            ans(path,pathlen)
        else:
            myfun(root.left,path,pathlen)
            myfun(root.right,path,pathlen)

def printPath(root):
    path = []
    return myfun(root,path,0)

import sys
sys.setrecursionlimit(1000000)
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
            currNode.left=Node(int(currVal)
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
        printPath(root)
        print()

