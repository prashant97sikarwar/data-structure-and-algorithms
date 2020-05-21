
def serialize(root, A):
    if root is None:
        A.append(-1)
        return
    A.append(root.data)
    serialize(root.left,A)
    serialize(root.right,A)
    
def deSerialize(A):
    index = 0
    if index == len(A):
        return None
    val = A[index]
    index += 1
    if A[index] == -1:
        return None
    node = Node(val)
    node.left = deSerialize(A)
    node.right = deSerialize(A)
    return node

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

def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)
    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        root=buildTree(input())
        A=[]
        serialize(root, A)
        r=deSerialize(A)
        inorder(r)
        print()
        
        
        