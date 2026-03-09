  
# Cube Root by Binary Search

def cuberoot_binary_search(n,precision):
    start_val = 0
    end_val = n
    if n == 0:
        return 0
    if n == 1: 
        return 1
    if n == -1:
       return -1
    if abs(n) >= 1:
        start_val = 0
        end_val = n
    elif abs(n) < 1:
        start_val=0
        end_val = 1   
    cnt =True
    while cnt:
        
        mid_val = (start_val+end_val)/2
        cube= mid_val * mid_val*mid_val
        if abs(cube - abs(n)) <=precision:
            cnt=False
            if n < 0:
                return -mid_val
            else:
                return mid_val
        elif cube> abs(n):
                end_val=mid_val
        else: 
            start_val = mid_val 
            