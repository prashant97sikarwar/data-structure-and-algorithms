def inorder( node): 
    current = node 
    while(current.left is not None): 
        current = current.left  
  
    return current 

def deleteNode(root, key): 
 
    if root is None: 
        return root  

    if key < root.data: 
        root.left = deleteNode(root.left, key) 
    elif(key > root.data): 
        root.right = deleteNode(root.right, key) 
  
    else: 

        if root.left is None : 
            temp = root.right  
            root = None 
            return temp  
              
        elif root.right is None : 
            temp = root.left  
            root = None
            return temp 

        temp = minValueNode(root.right) 
        root.data = temp.data
        root.right = deleteNode(root.right , temp.data) 
    return root  

class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
        

from collections import deque
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
    if root is not None: 
        inorder(root.left) 
        print (root.data, end=' '),
        inorder(root.right) 
    
    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        x=int(input())
        root=buildTree(s)
        root = deleteNode(root,x)
        inorder(root)
        print()