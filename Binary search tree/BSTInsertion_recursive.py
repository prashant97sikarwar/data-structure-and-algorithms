class TreeNode:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.val = data
        
def insertInBST(root,num):
    if root is None:
        root = TreeNode(num)
    else:
        if num > root.val:
            root.right = insertInBST(root.right,num)
        else:
            root.left = insertInBST(root.left,num)
    return root

def preorder(root):
    if root is None:
        return 
    print(root.val,end=" ")
    preorder(root.left)
    preorder(root.right)

print("enter number of nodes to be inserted")
n = int(input())
print("enter the nodes values to be inserted in the BST")
flag = False
for i in range(n):
    num = int(input())
    if flag == False:
        root = TreeNode(num)
        flag = True
    else:
        insertInBST(root,num)
print("preorder of BST is as follows")
preorder(root)
print()