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