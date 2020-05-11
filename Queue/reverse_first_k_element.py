
def reverseK(queue,k,n):
    stack = []
    for i in range(k):
        x = queue.pop(0)
        stack.append(x)
    while len(stack) != 0:
        y = stack.pop()
        queue.append(y)
    for i in range(n-k):
        x = queue.pop(0)
        queue.append(x)
    return queue

import atexit
import io
import sys


_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,k = map(int,input().strip().split())
        a = list(map(int,input().strip().split()))

        queue = [] 
        for i in range(n):
            queue.append(a[i]) 

        print(*reverseK(queue,k,n))
