def myfun(root1,root2):
    if root1 == None and root2 == None:
        return True
    elif (root1 == None and root2 != None) or (root2 == None and root1 != None):
        return False
    elif (myfun(root1.left,root2.right) == False) or (myfun(root2.left,root1.right) == False):
        return False
    return True

def IsFoldable(root):
    if root is None:
        return True
    return  myfun(root.left,root.right)

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
        if IsFoldable(root) is True:
            print('Yes')
        else:
            print('No')