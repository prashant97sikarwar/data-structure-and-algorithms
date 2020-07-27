def reversePrint(root):
    ans =[] 
    if root is None:
        return
    else:
        que = []
        que.append(root)
        while que:
            l = []
            count = len(que)
            while count > 0:
                kj = que.pop(0)
                l.append(kj.data)
                if kj.left is not None:
                    que.append(kj.left)
                if kj.right is not None:
                    que.append(kj.right)
                count -= 1
            ans.append(l)
    pq = ans[::-1]
    for i in range(len(pq)):
        for j in range(len(pq[i])):
            print(pq[i][j],end=' ')
            
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
        reversePrint(root)
        print()
            
