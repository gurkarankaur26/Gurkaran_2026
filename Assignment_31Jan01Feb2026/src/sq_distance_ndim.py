## Start: Function to calculate squared distance of n-dimension points
def sq_diftt_nd(p1,p2):
    len_p1 = len(p1)
    len_p2 = len(p2)
    #print(len_p1,len_p2)
    if len_p1 != len_p2:
        return 'Lists should be of same dimension'
    dist = 0
    for p1_i,p2_i in zip(p1,p2):
        dist = dist + (p1_i -p2_i)**2
    return dist
 ## End: Function to calculate squared distance of n-dimension points