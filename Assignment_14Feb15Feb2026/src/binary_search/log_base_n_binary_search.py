       
# Log Base n

def log_base_n(x, n,tol=1e-7):
    try:
     if x <= 0 :
         raise ValueError('Number must be greater than 0')
     if n <= 0 or n==1:
         raise ValueError('Base must be greater than 1')
     if x == 1:
         return 0.0
     if n > 1:
         low = 0
         high = 1
         while True  :
             high = high * 2
             #print('high',high)
             if n*high >= x:
                 break;
     elif n < 1:
         low =-1
         high = 0
         while True :
             low = low *2
             #print('low',low)
             if n**low <=x:
                 break;
     cnt = True
     while cnt:
         mid = (low+high)/2
         if abs(n**mid - x) < tol:
             cnt=False
             return mid
         if n**mid < x :
             low = mid
         else:
             high = mid
             
    except ValueError as e:
        print ("Error: ",e)
            
        