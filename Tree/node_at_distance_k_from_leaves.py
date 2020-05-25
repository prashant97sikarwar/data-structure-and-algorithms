def printKDistantfromLeafUtil(root, count, visited, pathLen, k):
    if root is None:
        return
    visited[pathLen] = False
    pathLen += 1
    
    if root.left is None and root.right is None and pathLen - k - 1 >= 0 and visited[pathLen-k-1] == False:
        count[0] += 1
        visited[pathLen -k - 1] = True
        return
    printKDistantfromLeafUtil(root.left, count, visited, pathLen, k)
    printKDistantfromLeafUtil(root.right, count, visited, pathLen, k)

def printKDistantfromLeaf(node, k):
    count = [0]
    visited = [False]*1000
    printKDistantfromLeafUtil(root, count, visited, 0, k)
    return count[0]

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
        k = int(input())
        print(printKDistantfromLeaf(root, k))