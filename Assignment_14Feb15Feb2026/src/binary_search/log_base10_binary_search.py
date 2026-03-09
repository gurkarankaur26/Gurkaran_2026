
# Log10 with Binary Search

def log10_binary_search(x, tol=1e-7):
    try:
     if x < 0 :
         raise ValueError('Number must be positive')
     if x == 1:
         return 0
     if x > 1:
         low = 0
         high = 1
         print('x>1',x)
         while True  :
             high = high * 2
             #print('high',high)
             if 10**high >= x:
                 break
     elif x < 1:
         low =-1
         high = 0
         while True :
             low = low *2
             #print('low',low)
             if 10**low <=x:
                 break
     cnt = True
     while cnt:
         mid = (low+high)/2
         if abs(10**mid - x) < tol:
             cnt=False
             return mid
         if 10**mid < x :
             low = mid
         else:
             high = mid
             
    except ValueError as e:
        print ("Error:",e)
            