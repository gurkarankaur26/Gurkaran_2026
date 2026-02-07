# Loops and Arrays exercises

'''Write a function `find_min_max(numbers)` that takes a list of numbers as input and returns a tuple `(minimum, maximum)`.'''

## Start MinMax function
def find_min_max(numbers):
    min =numbers[0]
    max =numbers[0]
    for i in numbers:
        if i < min:
            min=i
        elif i > max:
            max =i
    return(min,max)

## End: MinMax function


'''Write a function `min_max_normalize(value, data)` that:

* Takes two inputs:

  * `value`: the number you want to normalize
  * `data`: a list of numbers (dataset)
* Returns the normalized value of `value` using min-max normalization.'''

## Start: Function to normalise min max
def min_max_normalize(value, data):
    min,max=find_min_max(data)
    normalised_val= (value-min)/(max-min)
    return normalised_val

## End: Function to normalise min max


## Start: Function to compute mean/average of numbers in a list

def compute_mean(numbers):
    count =len(numbers)
    print(count)
    if count==0:
        return 0
    else:
        sum=0
        for i in numbers:
            sum = sum +i
        mean = sum/count
        return mean

## End: Function to compute mean/average of numbers in a list

'''Write a function `compute_sd(numbers)` that takes a list of numbers and returns the standard deviation.'''

## Start: Function to compute standard deviation of the list of numbers
import math
def compute_sd(numbers):
    mean = compute_mean(numbers)
    j=0
    for i in numbers:        
        numbers[j] =(i-mean)**2
        j=j+1
    sq_mean = compute_mean(numbers)
    sd=math.sqrt(sq_mean)
    return sd
## End: Function to comute standard deviation of the list of numbers

'''Write a function `find_outliers(nums, threshold)` that returns a list of numbers from `nums` that are outliers based on the given z-score threshold.

**Arguments:**

* `nums`: a list of numbers
* `threshold`: a number (like 2 or 3) representing how far from the mean we consider values as outliers'''

## Start : Function to find outliers

def find_outliers(nums, threshold):
    outliers=[]
    numbers=[]
    for i in nums:
        numbers.append(i)
    mean = compute_mean(numbers)
    sd = compute_sd(numbers)    
    #print(mean,sd)
    for i in nums:
       # print(i)
        z = (i-mean)/sd
        if z>threshold:
            outliers.append(i)
            #print(z)
    return outliers

## End: Function to find outliers


'''Write a function `compute_iqr(data)` that takes a list of numbers and returns the IQR.'''

## Start: Function to compute IntraquInterquartile Range  of the data

def compute_iqr(data):
    count = len(data)
    for i in range(count):
        for j in range(count-1):
            if data[j+1] < data[j]:
                temp=data[j]
                data[j]=data[j+1]
                data[j+1]=temp
    print('Sorted Data:'+str(data))
    Q1= int(count*25/100)
    #print(Q1)
    print('Q1:'+str(data[Q1]))
    Q3 = int(count*75/100)
    #print(Q3)
    print('Q3:'+str(data[Q3]))
    IQR = data[Q3]-data[Q1]    
    return (IQR)       
## End: Function to compute the intraquInterquartile Range of the data

'''Write a function `standardize(data)` that takes a list of numbers and returns a new list where each number is standardized.'''

## Start: Function Standardize the given data
def standardize(data):
    resList=[]
    dList=[]
    for i in data:
        dList.append(i)        
    mean = compute_mean(dList)
    sd = compute_sd(dList)
    #print(mean,sd)
    for j in data:
        if sd>0:                
            z = round((j-mean)/sd,4)
            #print(j-mean)
        else: z=0.0
        resList.append(z)
    return (resList)

## End: Function Standardize the given data


'''Write a function `compute_rmse(actual, predicted)` that:

* Takes two lists of equal length: `actual` and `predicted`.
* Returns the Root Mean Square Error between them.'''


## Start:Function to compute Root Mean Square Error (RMSE)

import math
def compute_rmse(actual, predicted):
    error=[]
    if len(actual) != len(predicted):
        return 'Data input has unequal elements'
    sum=0
    count=len(actual)
    for i in range(count):
        error.append((actual[i]-predicted[i])**2)
        print(error[i])
        sum =sum +error[i]
    avg = sum/count
    rmse = math.sqrt(avg)
    return rmse        
        

## End:Function to compute Root Mean Square Error (RMSE)

'''Write a function `compute_mae(actual, predicted)` that:

* Takes two lists of points (each point is a list of numbers, e.g. `[x, y, z, ...]`).
* Returns the mean absolute error across all dimensions.'''
## Start: *Compute Mean Absolute Error in N-Dimensions*
def compute_mae(actual, predicted):
    ln_ac = len(actual)
    ln_pre = len(predicted)
    if ln_ac != ln_pre:
        return 'Actual and Predicted list have unqual number of elements'
    if type(actual[0]) != type(predicted[0]):
        return 'Element Type should be same for Actual and Predicted lists'
    res=[]
    if isinstance(actual[0], list) == False:                    
         print ( str(type(actual[0])))
         tot=0    
         for i in range(ln_ac):
            res.append(abs(actual[i]-predicted[i]))
            tot = tot +res[i]
         mae = tot/ln_ac  
         return mae
    else:       
      total_ele = 0
      total = 0
      for i in range(ln_ac):
            if len(actual[i]) != len(predicted[i]):
                return "Inner lists must have same length"            
            for j in range(len(actual[i])):
                val = abs(actual[i][j] - predicted[i][j])
                total += val
                total_ele += 1   
      mae = total / total_ele
      return mae
            
                   
        
## End: *Compute Mean Absolute Error in N-Dimensions*


'''Write a function `compute_huber_loss(y_true, y_pred, delta)` that takes:

* `y_true`: a list of actual values
* `y_pred`: a list of predicted values
* `delta`: the threshold value

and returns the **average Huber loss**.'''
## Start: Function to calculate Huber Loss

def compute_huber_loss(y_actual,y_pred,delta):
    loss=[]
    for i,j in zip(y_actual,y_pred):
        error = i-j
        val=0
        if abs(error)<=delta:
            val = 0.5 * error**2
        else:
            val = abs(error)- 0.5 * delta**2
        loss.append(val)
    total=0
    for i in loss:
        total=total+i
    huber_loss = total/len(loss)
    return huber_loss

## End: Function to calculate Huber Loss


'''**Exercise:**
Write a function `closer_point(P, A, B)` that:

* Takes three points (`P`, `A`, and `B`) as lists of numbers (same length).
* Returns `"A"` if P is closer to A, `"B"` if P is closer to B, or `"Equal"` if the distances are the same.'''

## Start: Function to find the point is closer to which point for the given three points

import math
def closer_point(p,a,b):
    len_p = len(p)
    len_a = len(a)
    len_b = len(b)
    if len_p != len_a or len_p !=len_b:
        return('Points must have same dimension')        
    d_pa=0
    d_pb=0
    for pi,ai,bi in zip(p,a,b):
        d_pa =d_pa + (pi-ai)**2 
        d_pb = d_pb+(pi-bi)**2 
    #dis_pa =math.sqrt(d_pa)
    #dis_pb =math.sqrt(d_pb)
    if   d_pa < d_pb:
        return "A"
    elif d_pb < d_pa:
        return "B"
    else:
        return "Equal"
    
    

## End: Function to find the point is closer to which point for the given three points


'''Write a function `find_nearest_neighbour(numbers, target)` that returns the nearest neighbour of the target from the list.'''

## Start: Function to find the nearest neighbour in 1D

def find_nearest_neighbour_1d(numbers, target):
    prev_dis =(numbers[0]-target)**2
    n_p= numbers[0]
    for i in numbers:
        dis = (i-target)**2
        #print(i,target,dis)
        if dis < prev_dis:
            prev_dis =dis
            n_p = i
    return n_p

## End: Function to find the nearest neighbour in 1D


'''Write a function `find_nearest_neighbour(points, target)` that returns the point from the list `points` which is closest to the `target`.

* `points` is a list of `(x, y)` tuples.
* `target` is a tuple `(x, y)` representing the location we want to compare.
* The function should return the nearest neighbour point as a tuple.'''


## Start: Function to find the nearest neighbour in 2D


def find_nearest_neighbour_2d(numbers, target):
    min_dis =()
    prev_dis=0
    
    for j in numbers:         
        dis=0  
        for ji, bi in zip(j,target):            
            dis+=(ji-bi)**2
        #print(j,target,dis) 
        if min_dis ==() :
           #print('hi')
           min_dis =j 
           prev_dis=dis
        else:
          if dis < prev_dis:
            #print(dis)  
            min_dis=j        
    return(min_dis)   
    

## End: Function to find the nearest neighbour in 2D


'''Write a function `find_nearest_neighbour(point, points)` that takes:

* `point`: a list of numbers representing coordinates of a point in N-dimensions
* `points`: a list of points (each a list of numbers)

and returns the point from `points` that is nearest to `point`'''

## Start: Function to find the nearest neighbour in ND


## End: Function to find the nearest neighbour in ND



'''Write a function `multiply_polynomial(poly, num)` that takes:

* `poly`: a list of coefficients of the polynomial
* `num`: a number to multiply the polynomial with

The function should return a new list of coefficients after multiplication.'''

## Start: Function to multiply a number to polynomial
def multiply_polynomial(poly,num):
    res=[]
    for i in poly:
        res.append(i*num)
    return res        

## End: Function to multiply a number to polynomial

'''Write a function `add_polynomials(p1, p2)` that takes two lists `p1` and `p2`, representing two polynomials, and returns a new list with their sum.'''

## Start: Function to add two polynomials

def add_polynomials(p1, p2):
    len_p1 =len(p1)
    len_p2 =len(p2)
    p1 =p1[:]
    p2 =p2[:]
    if len_p1 != len_p2:
        diff =abs(len_p1-len_p2)
        if len_p1 < len_p2:
        # [0]-> list contating one element 0; [0]*diff-> repeats the list as per the number in diff
           p1 = [0]*diff+p1 
        elif len_p2 < len_p1:
           p2 = [0]*diff +p2 # + joins the two list
    print(p2)
    res=[]
    for i, j in zip(p1,p2):
        res.append(i+j)
    return res
## End: Function to add two polynomials

'''Write a function multiply_polynomials(p1, p2) that takes two lists of coefficients p1 and p2, and returns a new list representing their product.'''

## Start: Function to multiply two polynomials
def multiply_polynomials(p1, p2):
    len_p1 = len(p1)
    len_p2 = len(p2)    
    res_len = len_p1 + len_p2-1    
    # Result list filled with zeros
    result = [0] * res_len    
    for i in range(len_p1): 
        for j in range(len_p2): 
            result[i + j] += p1[i] * p2[j]  
    
    return result

## End: Function to multiply two polynomials

'''Write a function solve_for_first_variable(equation, vars) that returns the value of the first variable.
equation: a list of numbers where the first n elements are coefficients of the variables and the last element is the right-hand side value.
vars: a list of values for the last n−1 n−1 variables.'''

## Start : Function to solve first variable of a polynomial

def solve_for_first_variable(equation, vars):
    # `equation = [3, 4, 6, 20]` → coefficients and RHS value.
    # `vars = [5, 6]` → known variable values (in the same order as coefficients after the first one).
   
    len_eq = len(equation)
    len_pol = len_eq-1
    pol = equation[0:len_pol]
    b= equation[len_pol:]
    tot=0
    for i in range(len_pol):
        if i > 0:
          #print(pol[i],vars[i-1])
          tot = tot + pol[i]*vars[i-1]
    a1 = pol[0]
    x = (b[0] - tot)/a1 
    #print(a1,b[0],tot) 
    return x

## End: Function to solve first variable of a polynomial


