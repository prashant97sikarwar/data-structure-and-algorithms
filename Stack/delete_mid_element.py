import math
def deleteMid(s, sizeOfStack, current):
    mid = math.ceil(sizeOfStack/2)
    s.pop(mid-1)
    return s
