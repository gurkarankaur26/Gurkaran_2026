
## Start: Function to find the distance between two points
def distance(o1,o2):
    x1,y1=o1
    x2,y2=o2
    dist = (y2-y1)**2 +(x2-x1)**2 #abs(y1-y2)+abs(x1-x2)
    return dist

## End: Function to find the distance between two points

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

## Start: Function to find the  k closest neighbour in ND

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

## Start: Function to multiply a number to polynomial/equation

def multiply_eqn(poly,num):
    res=[]
    for i in poly:
        res.append(i*num)
    return res

## End: Function to multiply a number to polynomial/equation

## Start: Function to subtract a number two polynomial/equation

def subtract_eqn(eqn1,eqn2):
    res=[]
    for i,j in zip(eqn1,eqn2):
        res.append(i-j)
    return res

## End: Function to subtract two polynomial/equation

## Start: Function to multiple two polynomials/equations
def elementwise_mult(eqn1, eqn2):
    # eqn1 = [1, 2, 3]
    # eqn2 = [3, 4, 5]
    # result = [1*3, 2*4, 3*5]
    result = []
    for i, x in enumerate(eqn1):
        result.append(x * eqn2[i])
    return result

## End: Function to multiple two polynomials/equations

## Start:Function to Solve one variable in a Linear Equation

def solve1(eqns):
    eqn = eqns[0] # eqn = [3, 4]
    a, b = eqn # a = 3; b = 4
    return [b / a]

#eqns = [[3, 4]] # 3x = 4

## End: Function to Solve one variable in a Linear Equation

## Start:Function to eliminate a variable from an equations

# x + 3*y + 2*z = 20
# y, z = [5, -5]
# x = 20 - (3*5 + 2*-5)

#solve_x([4,3,2,7, 20], [5, -5, 8])
# 4x + 3*y + 2*z + 7u = 20
# y, z, u = [5, -5, 8]
# 4x = 20 - (3*5 + 2*-5 + 7*8)
# x = (20 - (3*5 + 2*-5 + 7*8))/4
def solve_x(eqn1, n_1_vars):
    eqn11 = eqn1[1:-1]
    rhs = eqn1[-1] - sum(elementwise_mult(eqn11, n_1_vars))
    return rhs / eqn11[0]

## End: Function to eliminate a variable from an equations


## Start: Function to solve two varaibles in a linear equation

# x + y = 10
# 2x + y = 15
eqns = [[1, 1, 10], [2, 1, 15]]

def solve2(eqns): 
    eqn1 = eqns[0] # First Equation
    eqn2 = eqns[1] # Second Equation
    mult = eqn2[0]/eqn1[0]
    eqn11 = multiply_eqn(eqn1, mult)
    eqn21 = subtract_eqn(eqn2, eqn11)[1:] # Subract both equations and remove x as it is 0
    n_1_vars = solve1([eqn21])
    x = solve_x(eqn1, n_1_vars) # y = 1, [1, 1, 10], x = 10-1*
    return [x] + n_1_vars

## End: Function to solve two variables in a linear equation

## Start: Function to solve three varaibles in a linear equation

def solve3(eqns): 
    if len(eqns) == 1:
         return solve1(eqns)
    eqn1 = eqns[0]
    # eliminate x by subtracting first eqn from second and third after mult coefficients
    new_eqns = []
    for eqn2 in eqns[1:]:
        mult = eqn2[0]/eqn1[0]
        eqn11 = multiply_eqn(eqn1, mult)
        neweqn = subtract_eqn(eqn2, eqn11)[1:]
        new_eqns.append(neweqn)
    # # we will be left 2 eqns and 2 var -> solve2()
    n_1_vars = solve2(new_eqns)
    x = solve_x(eqn1, n_1_vars) # y = 1, [1, 1, 10], x = 10-1*
    return [x] + n_1_vars


## End: Function to solve three varaibles in a linear equation

## Start: Function to solve n varaibles in a linear equation

def solven(eqns): 
    n_vars=[]
    x=[]    
    if len(eqns) == 1:
        a, b = eqns[0]
        return [(b / a)]
    eqn1 = eqns[0]
    # eliminate x by subtracting first eqn from rows below after mult coefficients    
    new_eqns = []
    for eqn2 in eqns[1:]:
        mult = eqn2[0]/eqn1[0]
        eqn11 = multiply_eqn(eqn1, mult)
        neweqn = subtract_eqn(eqn2, eqn11)[1:]
        new_eqns.append(neweqn)
    n_vars = solven(new_eqns)
    x =solve_x(eqn1,n_vars)
    return [x] + n_vars

## End: Function to solve n varaibles in a linear equation
    
    