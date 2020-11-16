class Node:
    def __init__(self, info):
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 
    def __str__(self):
        return str(self.info) 
def preOrder(root):
    if root == None:
        return
    print (root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)

class BinarySearchTree:
    def __init__(self): 
        self.root = None
    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            current = self.root
            while(True):
                if val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                elif val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                else:
                    break

            
tree = BinarySearchTree()
t = int(input())

print("provide input of values for which BST is constructed")
arr = list(map(int, input().split()))

for i in range(t):
    tree.insert(arr[i])
print("the preorder travesal of constructed BST is as follows")
preOrder(tree.root)