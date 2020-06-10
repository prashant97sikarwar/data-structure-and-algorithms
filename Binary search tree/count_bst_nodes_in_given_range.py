def getCountOfNode(root,l,h):
    if root is None:
        return 0 
    if root.data == l and root.data == h:
        return 1
    if root.data >= l and root.data <= h:
        return 1 + getCountOfNode(root.left,l,h) + getCountOfNode(root.right,l,h)
    elif root.data < l:
        return getCountOfNode(root.right,l,h)
    else:
        return getCountOfNode(root.left,l,h)
    
class Node:
    def __init__(self):
        self.data = 0
        self.left = None
        self.right = None


def createNewNode(value):
    temp=Node()
    temp.data=value
    temp.left=None
    temp.right=None
    return temp

def newNode(root,data):
    if(root is None):
        root=createNewNode(data)
    elif(data<root.data):
        root.left=newNode(root.left,data)
    else:
        root.right=newNode(root.right,data)
        
    return root
    
def main():
    testcases=int(input())
    while(testcases>0):
        root=None
        sizeOfArray=int(input())
        arr=[int(x) for x in input().strip().split()]
        for i in arr:
            root=newNode(root,i)
            
        lr=[int(x) for x in input().strip().split()]

        print(getCountOfNode(root,lr[0],lr[1]))
        testcases-=1

if __name__=="__main__":
    main()