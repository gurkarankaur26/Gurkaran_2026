## Start: Function to subtract a number two polynomial/equation

def subtract_eqn(eqn1,eqn2):
    res=[]
    for i,j in zip(eqn1,eqn2):
        res.append(i-j)
    return res

## End: Function to subtract two polynomial/equation