def inOrder(root):
    if root is None:
        return
    inOrder(root.left)
    print(root.data,end=' ')
    inOrder(root.right)
    
def main():
    testcases=int(input())
    while(testcases>0):
        root=None
        sizeOfArray=int(input())
        arr=[int(x) for x in input().strip().split()]
        for i in arr:
            root=newNode(root,i)
       
        inOrder(root)
        print()
      
        testcases-=1

if __name__=="__main__":
    main()
#} Driver Code Ends