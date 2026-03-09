from sq_distance import distance

## Start: Function to find the closest neighbour in 2D
def find_closest_2d(x_new,X,y,distance=distance):
    min=None    
    closest=None
    for i, xx in enumerate(X):
       # print(x_new,xx)
        diff = distance(x_new,xx)
        #print(diff)
        if min==None or diff < min:
            min=diff
            closest=i
        #print(closest)
    return y[closest]
## End: Function to find the closest neighbour in 2D