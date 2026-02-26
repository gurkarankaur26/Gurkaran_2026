
########## Vector Class with Turn Counter clockwise###############

import math
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
        
    def norm(v):
        return math.sqrt(v.y**2+v.x**2)
    
    def turn(self,theta_ccw):        
        v_new_x = self.x * round(math.cos(math.radians(theta_ccw)), 5) - self.y * round(math.sin(math.radians(theta_ccw)), 5)
        v_new_y = self.x * round(math.sin(math.radians(theta_ccw)), 5) + self.y * round(math.cos(math.radians(theta_ccw)), 5)
        return Vector(v_new_x,v_new_y)
        
       
        
    
########################Matrix Multiplication ################################

def matmult(A,B):
    r_mat=[]
    
    row_a = len(A)
    row_b = len(B)
    col_a = len(A[0])
    col_b = len(B[0])       
    #r_mat(0,0)  = A[0][0]*B[0][0]+A[0][1]*B[1][0]+A[0][2]*B[2][0]
    if col_a != row_b:
        raise ValueError("Cannot multiply: A cols != B rows")
    for i in range(row_a):
        row =[] 
        for j in range(col_b):
            row.append(0)
            #print(row)
        r_mat.append(row)
    #print(r_mat)
    for i in range (row_a):
        for j in range(col_b):
         for k in range (row_b):
             r_mat[i][j]= r_mat[i][j]+A[i][k]*B[k][j]
    return r_mat

################## DOT PRODUCT #################################

def dotprod(A,B):
    prod = A.x*B.x +A.y*B.y
    return prod
            
###############   BINARY TREE #####################################

class Node:
    left = None
    right = None
    def __init__(self, val):
        self.val = val
    def printa(self):
        if self.left:
            self.left.printa()
        if self.right:
            self.right.printa()
        print(self.val)
    def search(self, value): # True or false
        # Fix me
        if value < self.val:            
            if self.left:
                return self.left.search(value)
            elif self.right:
                return self.right.search(value)
        elif value == self.val:
            return True
        else:
            if self.left:
                return self.left.search(value)
            elif self.right:
                return self.right.search(value)
        
        
    #################### JOB OFFER DECISION TREE #########################
    
class DT:
    def __init__(self, boundary=None, boundary_val=None, left=None, right=None,decision =None):
        self.boundary = boundary
        self.boundary_val = boundary_val
        self.left = left 
        self.right = right 
        self.decision =decision
    def YES():
          return DT(decision=True)
    def NO():
          return DT(decision=False)  
    def check(self, features:dict):
        if self.left == None and self.right==None:
            if self.decision == None:
               raise ValueError("Leaf node is missing")
            else:
                return self.decision  
        # Feature validation
        if self.boundary not in features:
            raise ValueError(f"Feature '{self.boundary}' is  missing")
        if features[self.boundary] <= self.boundary_val:
            if self.left:
              return self.left.check(features)
            else:
             raise ValueError("Left node is missing")
        elif features[self.boundary] > self.boundary_val:             
             if self.right:
                return self.right.check(features)
             else:
                raise ValueError("Right node is missing")
        else: 
         return self.decision
            
            