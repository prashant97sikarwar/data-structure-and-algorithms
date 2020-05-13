from sys import *
class node:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.data = val

def other(que,left,right):
    if left is None or right is None:
        return None
    if left.data == que:
        return right.data
    if right.data == que:
        return left.data

    des = other(que,left.left,right.right)
    if des is not None:
        return des
    
    deslk = other(que,left.right,right.left)
    if deslk is not None:
        return deslk


def mirror(root,que):
    if root is None:
        return None
    if root.data == que:
        return que
    return other(que,root.left,root.right)
n,q = map(int,stdin.readline().split())
arr = [node(i) for i in range(1,n+1)]
for i in range(n-1):
    p,c,info = stdin.readline().split()
    parent = arr[int(p) - 1]
    child = arr[int(c) - 1]
    if info == 'R':
        parent.right = child
    if info == 'L':
        parent.left = child
    root = arr[0]
for i in range(q):
    que = int(input())
    ans = mirror(root,que)
    if ans == None:
        print(-1)
    else:
        print(ans)

