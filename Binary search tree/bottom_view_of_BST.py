def function(root,hd,d):
    if root is None:
        return
    try:
        d[hd].append(root.data)
    except:
        d[hd] = [root.data]
    function(root.left,hd - 1,d)
    function(root.right,hd + 1,d)
        

def verticalOrder(root):
    d = {}
    hd = 0
    function(root,hd,d)
    for index,values in enumerate(sorted(d)):
        for i in d[values]:
            print(i,end=' ')
            

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
        verticalOrder(root)
        print()