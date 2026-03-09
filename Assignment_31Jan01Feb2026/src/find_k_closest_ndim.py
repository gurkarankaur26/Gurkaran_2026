
## Start: Function to find the  k closest neighbour in ND
from sq_distance_ndim import sq_diftt_nd
def find_k_closest_nd(x_new,X,y,k=2,distance=sq_diftt_nd):  
     
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

## End: Function to find the  k closest neighbour in ND