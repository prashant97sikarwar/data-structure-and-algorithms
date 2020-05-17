def myfun(root):
    if root is None:
        return root

    if root.left:
        left = myfun(root.left)

        while left.right:
            left = left.right
        left.right = root
        root.left = left

    if root.right:
        right = myfun(root.right)

        while right.left:
            right = right.left
        right.left = root
        root.right = right
    return root


def bToDLL(root):
    if root is None:
        return root

    root = myfun(root)

    while root.left:
        root = root.left
    return root


from collections import deque
class Node:
    """ Class Node """
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
   
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

import sys            
def printDLL(head):
    prev = None
    sys.stdout.flush()
    while(head != None):
        print(head.data, end=" ")
        prev=head
        head=head.right
    print('')
    while(prev != None):
        print(prev.data, end=" ")
        prev=prev.left
    print('')
    
if __name__=='__main__':
    t=int(input())
    for _ in range(0,t):
        s=input()
        root=buildTree(s)
        head = bToDLL(root)
        printDLL(head)
