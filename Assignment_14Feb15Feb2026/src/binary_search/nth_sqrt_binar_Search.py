         
# Compute Nth root

import math
def compute_nth_root(x,n):
    start_val = 0
    end_val = x
    if x == 0:
        return 0
    if x == 1: 
        return 1
    if x == -1:
       return -1
    if abs(x) >= 1:
        start_val = 0
        end_val = x
    elif abs(x) < 1:
        start_val=0
        end_val = 1   
    cnt =True
    while cnt:        
        mid_val = (start_val+end_val)/2
        val= 1
        for i in range (n):
            val = val*mid_val
        if abs(val - abs(x)) <=1e-6:
            cnt=False
            if x < 0:
                return -mid_val
            else:
                return mid_val
        elif val> abs(x):
                end_val=mid_val
        else: 
            start_val = mid_val 
            
