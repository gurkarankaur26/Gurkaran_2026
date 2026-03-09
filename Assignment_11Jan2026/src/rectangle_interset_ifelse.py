def are_rectangles_intersecting(rect1: tuple, rect2: tuple):    
    x1y1 = rect1[0]
    x2y2 = rect1[1]
    x1 = x1y1[0]
    y1 = x1y1[1]
    x2= x2y2[0]
    y2 = x2y2[1]
    p1q1 = rect2[0]
    p2q2 = rect2[1]
    p1 = p1q1[0]
    q1 = p1q1[1]
    p2 = p2q2[0]
    q2 = p2q2[1]    
    if(p1 > x1 and p2 <x2 and q1>y1 and q2<y2) or ( p1>x1 and q1==y1 and p2>x2 and q2 >y2)or (x2==p1 and y2 == q1 and x2 < p2 and y2 < q2) or (p1<x2 and q1 <y2 and x2 < p2 and y2 <q2):
        return True
    else: 
        return False
    
    