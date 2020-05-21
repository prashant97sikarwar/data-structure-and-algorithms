def levelOrder(root):
    if root is None:
        return
    q = []
    q.append(root)
    while q:
        temp = q.pop(0)
        print(temp.data,end=' ')
        if temp.left:
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)

def main():
    testcases=int(input())
    while(testcases>0):
        root=None
        sizeOfArray=int(input())
        arr=[int(x) for x in input().strip().split()]
        for i in arr:
            root=newNode(root,i)
       
        levelOrder(root)
        print()
        testcases-=1

if __name__=="__main__":
    main()