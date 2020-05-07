class point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
def onsegment(p,q,r):
    if q.x >= min(p.x,r.x) and q.x <= max(p.x,r.x) and q.y >= min(p.y,r.y) and q.y <= max(p.y,r.y):
        return True
    return False
def check(p,q,r):
    val = (float(q.y - p.y) * (r.x - q.x)) - (float(q.x - p.x) * (r.y - q.y))
    if val > 0:
        return 1
    if val < 0:
        return 2
    if val == 0:
        return 0
def intersect(p1,q1,p2,q2):
    o1 = check(p1,q1,p2)
    o2 = check(p1,q1,q2)
    o3 = check(p2,q2,p1)
    o4 = check(p2,q2,q1)
    if o1 != o2 and o3 != o4:
        return True
    if o1 == 0 and onsegment(p1,p2,q1):
        return True
    if o2 == 0 and onsegment(p1,q2,q1):
        return True
    if o3 == 0 and onsegment(p2,p1,q2):
        return True
    if o4 == 0 and onsegment(p2,q1,q2):
        return True

    

t = int(input())
while t > 0:
    x1,y1,x2,y2 = map(int,input().split())
    x3,y3,x4,y4 = map(int,input().split())
    p1 = point(x1,y1)
    q1 = point(x2,y2)
    p2 = point(x3,y3)
    q2 = point(x4,y4)
    if intersect(p1,q1,p2,q2):
        print(1)
    else:
        print(0)
    t -= 1
    
    