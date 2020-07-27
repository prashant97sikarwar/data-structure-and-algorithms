class Codec:
    def serialhelp(self,root,path):
        if root is None:
            path.append("None")
            return
        else:
            path.append(str(root.val))
            self.serialhelp(root.left,path)
            self.serialhelp(root.right,path)
            
    def help2(self,data):
        if data[0] == "None":
            data.pop(0)
            return
        else:
            node = TreeNode(data[0])
            data.pop(0)
            node.left = self.help2(data)
            node.right = self.help2(data)
        return node
    
    def serialize(self, root):
        path = []
        if root is None:
            return []
        else:
            self.serialhelp(root,path)
            path = ','.join(path)
        return path
        

    def deserialize(self, data):
        if not data:
            return
        else:
            data = data.split(',')
            return self.help2(data)
            

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
        
        
        