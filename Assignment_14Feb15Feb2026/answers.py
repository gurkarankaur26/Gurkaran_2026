import math

class LineModel:#y =mx +c
    def fit(self,data):
          x1,y1 = data[0]
          x2,y2 = data[1]          
         # y1 = m*x1 + c
         # y2 = m*x2 + c
          self.m= (y2-y1)/(x2-x1)
          self.c= y1 - (self.m)*x1
    def predict(self,x_new):
        return x_new*self.m + self.c
######################################################################## 
    
class Vector:
    def __init__(self,m,n):
        self.x=m
        self.y=n
    def add(self, v):
        p = self.x+ v.x
        q= self.y+v.y         
        return (Vector(p,q))
    def multiply(self, n):
        if type(n) == int or type(n)== float:
            return (Vector(n*self.x,n*self.y))
        
    def dist(self, v):
        return math.sqrt((self.y - v.y)**2+  (self.x - v.x)**2)
    
    def turn(self,theta_ccw):        
        v_new_x = self.x * round(math.cos(math.radians(theta_ccw)), 5) - self.y * round(math.sin(math.radians(90)), 5)
        v_new_y = self.x * round(math.sin(math.radians(90)), 5) + self.y * round(math.cos(math.radians(theta_ccw)), 5)
        #print(round(math.cos(math.radians(90)), 5), round(math.sin(math.radians(90)), 5))
        return Vector(v_new_x,v_new_y)
    
'''#####################################################################################
                                 BINARY SEARCH
   ###################################################################################### '''
   
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
                 break;
     elif x < 1:
         low =-1
         high = 0
         while True :
             low = low *2
             #print('low',low)
             if 10**low <=x:
                 break;
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
        print (f("Error:{e}"))
            
        
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
        print (f("Error:{e}"))
            
        