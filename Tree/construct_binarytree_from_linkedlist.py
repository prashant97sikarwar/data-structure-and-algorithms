
def convert(head):
    q = []
    if head is None:
        return None
    root = Tree(head.data)
    q.append(root)
    head = head.next
    while head: 
        temp = q.pop(0)
        temp.left = Tree(head.data)
        q.append(temp.left)
        head = head.next
        if head:
            temp.right = Tree(head.data)
            q.append(temp.right)
            head = head.next
    return root

import atexit
import io
import sys

class ListNode:

    
    def __init__(self, data):
        self.data = data
        self.next = None


class Tree:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Conversion:
    def __init__(self, data=None):
        self.head = None
        self.root = None

    def push(self, new_data):

        new_node = ListNode(new_data)

        new_node.next = self.head

        self.head = new_node

    def levelorderTraversal(self, root):
        mylist = []  
        if root is None:
            return
        que = []
        que.append(root)
        while True:
            n = len(que)
            if n == 0:
                break
            while (n > 0):
                node = que.pop(0)
                mylist.append(node.data)
                if node.left is not None:
                    que.append(node.left)
                if node.right is not None:
                    que.append(node.right)
                n -= 1
        mylist = mylist[::-1]
        print(*mylist)
        return


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        a = list(map(int, input().strip().split()))
        mylist = Conversion()  
        for i in range(n):
            mylist.push(a[i]) 
        root = convert(mylist.head)
        mylist.levelorderTraversal(root)

