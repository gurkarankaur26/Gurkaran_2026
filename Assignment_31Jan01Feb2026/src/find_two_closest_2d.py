from  sq_distance import distance
## Start: Function to find the 2 closest neighbour in 2D
def find_2_closest_2d(x_new,X,y,distance=distance):
    min=None    
    closest1=None
    closest2=None
    for i, xx in enumerate(X):
        #print(x_new,xx)
        diff = distance(x_new,xx)
        #print(diff)
        if min==None or diff < min:
            min=diff
            closest1=i    
    min =None
    for i, xx in enumerate(X):
        if i != closest1:
            diff = distance(x_new,xx)
            #print(diff)
            if min==None or diff < min:
                min=diff
                closest2=i
        else:
            continue
    avg = (y[closest1] + y[closest2])/2         
        #print(closest)
    return closest1, closest2,y[closest1],y[closest2],avg
## End: Function to find the closest neighbour in 2D