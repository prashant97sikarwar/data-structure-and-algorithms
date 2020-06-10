def getNode( data):  
    newNode = Node(data) 
    newNode.data = data 
    newNode.left = None
    newNode.right = None
    return newNode 

def LevelOrder(root , data): 
    if(root == None): 
        root = getNode(data) 
        return root 
      
    if(data <= root.data): 
        root.left = LevelOrder(root.left, data) 
    else: 
        root.right = LevelOrder(root.right, data) 
    return root      
  
def constructBst( arr, n): 
    if(n == 0): 
        return None
    root = None
  
    for i in range(0,n): 
        root = LevelOrder(root , arr[i]) 
      
    return root 

class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

    
def preOrder(root):
    if root is None:
        return 
    print(root.data,end=" ")
    preOrder(root.left)
    preOrder(root.right)
    
def main():
    testcases=int(input())
    while(testcases>0):
        root=None
        sizeOfArray=int(input())
        arr=[int(x) for x in input().strip().split()]
      
        root=constructBst(arr,sizeOfArray)
        
        preOrder(root)
        print()
       
        testcases-=1

if __name__=="__main__":
    main()