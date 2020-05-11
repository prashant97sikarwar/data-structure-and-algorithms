
def knows(a,b):
    if m[a][b] == 1:
        return True
    else:
        return False
def getId(m,n):
    a = 0
    b = n-1
    while a < b:
        if knows(a,b):
            a += 1
        else:
            b -= 1
    for i in range(n):
        if ((i != a) and (knows(a,i) or (not knows(i,a)))):
            return -1
    return a



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
        n = int(input())
        a = list(map(int,input().strip().split()))
        k = 0
        m = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(a[k])
                k+=1
            m.append(row)
        print(getId(m,n))