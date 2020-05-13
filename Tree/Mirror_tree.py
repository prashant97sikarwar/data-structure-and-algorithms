def mirror(root):
    if root is None:
        return
    mirror(root.left)
    mirror(root.right)
    temp = root.left
    root.left = root.right
    root.right = temp

from collections import deque
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


def inorderTraversalUtil(root):
    if root is None:
        return
    inorderTraversalUtil(root.left)
    print(root.data, end=' ')    
    inorderTraversalUtil(root.right)

def inorderTraversal(root):
    inorderTraversalUtil(root)
    print()
    
  
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
        mirror(root)
        inorderTraversal(root)
        
