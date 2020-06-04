def fun(root,x,s):
    if root is None:
        return False
    if fun(root.left,x,s):
        return True
    if s and (x - root.key) in s:
        return True
    else:
        s.add(root.key)
    return fun(root.right,x,s)
    
def findPair(root,x):
    s = set()
    return fun(root,x,s)

class Node:
    def __init__(self,val):
        self.key = val
        self.left = None
        self.right = None

hash = set()
class BSTree:
    def __init__(self):
        self.root = None

    def Insert(self,x):
        if self.root is None:
            self.root = Node(x)
            return
        curr_node = self.root
        while curr_node:
            if curr_node.key < x: # go to right subtree if value is more
                if curr_node.right is None:
                    break
                curr_node = curr_node.right
            elif curr_node.key > x:   #  go to left subtree if value is more.
                if curr_node.left is None:
                    break
                curr_node = curr_node.left
            else:
                return 

        if curr_node.key < x:
            curr_node.right = Node(x)
        else:
            curr_node.left = Node(x)
        return

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())  # number of nodes in tree
        a = list(map(int, input().strip().split()))  # parent child info in list
        x = int(input())
        # construct the tree according to given list
        tree = BSTree()
        for value in a:
            tree.Insert(value)  # Insert the nodes in tree.
        if findPair(tree.root,x):
            print(1)
        else:
            print(0)
        hash = set()