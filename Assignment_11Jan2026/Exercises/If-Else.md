### Start: Function to find the point closer to point p

Write a function `closer_point(p, a, b)` that takes:

* `p`: a tuple representing the coordinates of point P
* `a`: a tuple representing the coordinates of point A
* `b`: a tuple representing the coordinates of point B

The function should return:

* `'A'` if P is closer to A
* `'B'` if P is closer to B
* `'Equal'` if the distances are the same

def closer_point(p, a, b):
    x1 = p[0]
    y1 = p[1]
    x2 = a[0]
    y2 = a[1]
    x3 = b[0]
    y3 = b[1]
    d_pa = (x2-x1)**2 + (y2-y1)**2
    d_pb = (x3-x1)**2 + (y3-y1)**2
    if d_pa < d_pb:
        return('A')
    elif d_pb < d_pa:
        return('B')
    else:
        return('Equal')


### End: Function to find the point closer to point p

### Start: Function to check if point lies on the line segment
Write a function `is_point_on_line_1d(a, b, p)` that returns `True` if point `p` lies on the line segment between `a` and `b`, and `False` otherwise.

def is_point_on_line_1d(a, b, p):
    if p>=a and p <=b:
        return True
    else:
        return False


### End: Function to check if point lies on the line segment

### Start: Function to check if line segments are overlapping, touching, separate

Write a function `are_lines_touching_or_overlapping(start1, end1, start2, end2)` that returns `True` if the two 1D line segments are overlapping or touching, and `False` if they are completely separate.

📌 Make sure your function works correctly even if the start is greater than the end — the order shouldn't matter.

def are_lines_touching_or_overlapping(start1, end1, start2, end2):
    if (start1 <= start2 and start2 <= end1 and end1 <= end2) or (start1 <= start2 and start2 <=end1 and end1 <=end2):#overlap
        return True
    elif end1 == start2: #touch
        return True
    elif start1 < end1 and start2 < end2 and end1 != start1:
        return False
    

### End: Function to check if line segments are overlapping, touching, separate

### Start: Function to check if a point lies inside or on the boundary of a rectangle

Write a function `is_point_inside_rectangle(x1, y1, x2, y2, px, py)` that returns `True` if the point `(px, py)` lies inside or on the boundary of the rectangle defined by corners `(x1, y1)` and `(x2, y2)`, and `False` otherwise.

def is_point_inside_rectangle(x1, y1, x2, y2, px, py):
    if (px >=x1 and py==y1) or (px > x1 and px <=x2 and py>y1 and py <=y2):
        return True
    else: 
        return False


### End: Function to check if a point lies inside or on the boundary of a rectangle

### Start: Function to check the rectangles are intersecting or not 
Write a function `are_rectangles_intersecting(rect1, rect2)` that takes two rectangles and returns `True` if they intersect, otherwise returns `False`.

Each rectangle is represented as a tuple of two points:
`((x1, y1), (x2, y2))`, where

* `(x1, y1)` is the **bottom-left corner**
* `(x2, y2)` is the **top-right corner**

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
    
    

### End: Function to check the rectangles are intersecting or not 
