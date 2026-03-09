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
    
    def turn(self,theta_ccw):        
        v_new_x = self.x * round(math.cos(math.radians(theta_ccw)), 5) - self.y * round(math.sin(math.radians(90)), 5)
        v_new_y = self.x * round(math.sin(math.radians(90)), 5) + self.y * round(math.cos(math.radians(theta_ccw)), 5)
        #print(round(math.cos(math.radians(90)), 5), round(math.sin(math.radians(90)), 5))
        return Vector(v_new_x,v_new_y)