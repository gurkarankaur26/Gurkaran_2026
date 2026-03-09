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
            
            