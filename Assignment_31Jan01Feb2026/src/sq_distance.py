## Start: Function to find the distance between two points
def distance(o1,o2):
    x1,y1=o1
    x2,y2=o2
    dist = (y2-y1)**2 +(x2-x1)**2 #abs(y1-y2)+abs(x1-x2)
    return dist

## End: Function to find the distance between two points