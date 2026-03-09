
# Square Root with Binary Search

def sqrt_binary_search(n,precision):
    start_val = 0
    end_val = n
   
    cnt =True
    while cnt:
        
        mid_val = (start_val+end_val)/2
        sroot= mid_val * mid_val
        if abs(sroot - n) <=precision:
            cnt=False
            return mid_val
        elif sroot> n:
                end_val=mid_val
        else: 
            start_val = mid_val 
        
    