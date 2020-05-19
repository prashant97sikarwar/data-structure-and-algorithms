def search(arr, strt, end, value): 
    i = 0
    for i in range(strt, end + 1): 
        if (arr[i] == value):  
            break
    return i 


def buildUtil(In, post, inStrt, inEnd, pIndex): 
    if (inStrt > inEnd):  
        return None
 
    node = Node(post[pIndex[0]])  
    pIndex[0] -= 1
  
    if (inStrt == inEnd):  
        return node  

    iIndex = search(In, inStrt, inEnd, node.data)  
  
    node.right = buildUtil(In, post, iIndex + 1,  
                                  inEnd, pIndex)  
    node.left = buildUtil(In, post, inStrt,  
                        iIndex - 1, pIndex)  
  
    return node 
  
def buildTree(In, post, n):
    pIndex = [n - 1]  
    return buildUtil(In, post, 0, n - 1, pIndex) 
    
import atexit
import io
import sys
from collections import  defaultdict

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

def preOrder(node):
    if node == None:
        return
    print(node.data, end=" ")
    preOrder(node.left)
    preOrder(node.right)
    
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())  
        in_order = list(map(int, input().strip().split()))  
        post_order = list(map(int, input().strip().split()))  
        preOrder(buildTree(in_order,post_order,n))
        print()