def createTree(parent,n):
    if len(parent) == 0:
        return
    else:
        arr = [Node(i) for i in range(n)]
        for i in range(n):
            if parent[i] == -1:
                root = arr[i]
            else:
                node = arr[parent[i]]
                if node.left is None:
                    node.left = arr[i]
                else:
                    node.right = arr[i]
        return root

import atexit
import io
import sys
from collections import  defaultdict

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
def traverse_level_order(root):
    if root is None:
        return
    que = []
    que.append(root)
    while 1:
        n = len(que)
        if n==0:
            break
        sorted_nodes = [node.key for node in que]
        sorted_nodes.sort()
        print(*sorted_nodes,end=" ")
        while(n>0):
            node = que.pop(0)
            if node.left != None:
                que.append(node.left)
            if node.right != None:
                que.append(node.right)
            n-=1

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input()) 
        a = list(map(int, input().strip().split())) 
        traverse_level_order(createTree(a,n))
        print()