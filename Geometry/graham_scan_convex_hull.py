from math import acos, sqrt, hypot


def find_length(a, b):
    return hypot(a[0] - b[0], a[1] - b[1])


def find_angle(a, b, c):
    
    ab = find_length(a, b)
    bc = find_length(b, c)
    ac = find_length(a, c)

    return round(acos((ab ** 2 + ac ** 2 - bc ** 2) / (2 * ab * ac)), 13)


def clockwise(a, b, c):
   
    rotate = (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])
    return rotate / abs(rotate) if rotate else 0


def checkio(points):
    p0 = min(points)
    result = [p0]
    stack = [p[:] for p in points]
    stack.remove(p0)
    stack.sort(key=lambda x: [find_angle(p0, [p0[0], max(x[1], p0[1] + 1)], x),
                              -find_length(p0, x)],reverse=True)
    p1 = stack.pop()
    result.append(p1)
    p2 = stack.pop()
    while True:
        rotate = clockwise(p0, p1, p2)
        if rotate > 0:
            
            result.pop()
            p0, p1, p2 = result[-2], result[-1], p2
            continue
        if not rotate:
            p1, p2 = sorted([p2, p1], key=lambda x: find_length(p0, x))
            result[-1] = p1
        result.append(p2)
        p0, p1 = p1, p2
        if not stack:
            break
        p2 = stack.pop()
    return [points.index(p) for p in result]
    
t = int(input())
while t > 0:
    z = int(input())
    arr = list(map(int,input().split()))
    points = []
    for i in range(0,2*z,2):
        points.append([arr[i],arr[i+1]])
    
    h = checkio(points)
    points.sort()
    for i in h:
        print(points[i],end=' ')
    print()
    t -= 1
    
