def floor(root,key):
    res = None
    while root is not None:
        if root.data == key:
            res = root.data
            return res
        elif root.data > key:
            root = root.left
        else:
            res = root.data
            root = root.right
    return res

class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None

class Tree:
    def createNode(self, data):
        return Node(data)
    
    def insert(self, node, data):
        if node is None:
            return self.createNode(data)
        else:
            if data < node.data:
                node.left = self.insert(node.left, data)
            else:
                node.right = self.insert(node.right, data)
            return node
        
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n=int(input())
        arr = input().strip().split()
        root = None
        tree = Tree()
        root = tree.insert(root, int(arr[0]))
        for j in range(1, n):
            root = tree.insert(root, int(arr[j]))
    
        key = int(input())
        
        ans=floor(root,key)
        if ans:
            print(ans)
        else:
            print(2147483647)