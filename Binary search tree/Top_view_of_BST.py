def fun(root,d,l,m):
    if root is None:
        return
    if d not in m:
        m[d] = [root.data,l]
    elif m[d][1] > l:
        m[d] = [root.data,l]
    fun(root.left,d-1,l+1,m)
    fun(root.right,d+1,l+1,m)
    
    

def topView(root):
    d = 0
    l = 0
    m = {}
    fun(root,d,l,m)
    for i in sorted(m.keys()):
        print(m[i][0],end=' ')

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
    
    


if __name__ == '__main__':
    t=int(input())
    for _ in range(0,t):
        root=make_tree()
        topView(root)
        print()