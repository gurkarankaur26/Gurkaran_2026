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
    