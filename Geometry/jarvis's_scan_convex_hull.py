class point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
def check(p,q,r):
    val = (float(q.y - p.y) * (r.x - q.x)) - (float(q.x - p.x) * (r.y - q.y))
    if val > 0:
        return 1
    if val < 0:
        return 2
    if val == 0:
        return 0
        
def min_index(points):
    mn = 0
    for i in range(1,len(points)):
        if points[i].x < points[mn].x:
            mn = i
        elif points[i].x == points[mn].x:
            if points[i].y > points[mn].y:
                mn = i
    return mn
    
def convexhull(points,n):
    if n < 3 : 
        print(-1)
    l = min_index(points)
    hull = []
    p = l
    q = 0
    while (True):
        hull.append(p)
        q = (p+1)%n
        for i in range(n):
            if check(points[p],points[i],points[q]) == 1:
                q =i
        p = q
        if p == l:
            break
    for each in hull:
        print(points[each].x, points[each].y)
t = int(input())
while t > 0:
    z = int(input())
    arr = list(map(int,input().split()))
    points = []
    for i in range(0,2*z,2):
        points.append(point(arr[i],arr[i+1]))
    n = len(points)
    convexhull(points,n)
    t -= 1
    