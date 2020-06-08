def findCeil(root, inp):
    res = -1
    while root is not None:
        if root.key == inp:
            return root.key
        elif root.key > inp:
            res = root.key
            root = root.left
        else:
            root = root.right
    return res

class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None

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
                return # no duplicate is to be inserted

        # insert key at the leaf position.
        if curr_node.key < x:
            curr_node.right = Node(x)
        else:
            curr_node.left = Node(x)
        return


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())  
        a = list(map(int, input().strip().split()))  
        x = int(input())
        tree = BSTree()
        for value in a:
            tree.Insert(value)  
        print(findCeil(tree.root,x))