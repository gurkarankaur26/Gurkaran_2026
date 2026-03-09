from sq_distance import distance
## Start: Function to find the k closest neighbour in 2D
def find_k_closest_2d(x_new,X,y,k=2,distance=distance):
       
    closest=None
    prev_closest = None
    tot = 0
    for j in range(k):  
        min=None      
        for i, xx in enumerate(X):           
            if i != prev_closest or closest==None:
                #print("i,prev_closest",i,prev_closest)                             
                diff = distance(x_new,xx) 
                #print(diff)             
                if min==None or diff < min:
                    min=diff
                    closest=i 
            else:
                continue
        #print(tot,y[closest] )
        tot = tot+y[closest] 
        prev_closest=closest  
    
    avg = tot/k       
    return avg

## Start: Function to find the k closest neighbour in 2D