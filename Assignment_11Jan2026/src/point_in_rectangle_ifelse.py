def is_point_inside_rectangle(x1, y1, x2, y2, px, py):
    if (px >=x1 and py==y1) or (px > x1 and px <=x2 and py>y1 and py <=y2):
        return True
    else: 
        return False