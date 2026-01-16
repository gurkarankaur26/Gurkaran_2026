

Write a function named `calculate_interest` that takes the following three arguments:

* `principal` (amount of money deposited or borrowed),
* `rate` (rate of interest per year, as a percentage),
* `time` (duration in years),

and returns the simple interest calculated using the formula above.

## Start: Function to calculate Simple Interest
def calculate_interest(p,r,t):                        
    si= (p*r*t)/100
    return(si)

## End: Function to calculate Simple Interest


## Start: Calculate Hypotense
def calculate_hypotenuse(base,height):
    hypotenuse = (base**2 + height**2) ** 0.5
    return hypotenuse
## End: Calculate Hypotense

# Start: Calculate distance between two points 2D
Write a function `find_distance_2d(x1, y1, x2, y2)` that returns the distance between the two points. Use the formula mentioned above. You can use the `math.sqrt` function to calculate the square root.

def find_distance_2d(x1,y1,x2,y2):   
    x = x2 - x1    
    y = y2 -y1
    #print(x,y)
    distance = (x**2 +y**2)**0.5
    return distance
# Start: Calculate distance between two points 2D

# Start: Calculate distance between two 3D points
Write a function called `calculate_distance_3d(x1, y1, z1, x2, y2, z2)` that returns the distance between two 3D points.

* The function should return the result as a float.
* You can use the built-in `math.sqrt()` function to calculate the square root.

In a room  we have length (x axis), width(y axis) and height(z axis)

      _________
     /     *b /|
    |--------| |-->z axis
    |        | |
    | *a---*c| /
    |        |/ /->y axis
    |--------|
     <--x-->

z axis : height 

Point A(x1,x2) Point C(x2,y2)  Point B(z1,z2) 
Now we want to calculate distance between Point A and Point B

Now A and C are on x,y axis,D(a,c) = Distance between A and C is as per 2D formula.
x = x2-x1
y = y2-y1
z = z2-z1
D(a,c)= d1= (x**2 + y**2)**0.5
Distance between c and b is the height i.e. z
D(a,b)= distance=  (d1**2 + z**2)**0.5

def calculate_distance_3d(x1, y1, z1, x2, y2, z2):
   x = x2-x1
   y = y2-y1
   z = z2-z1
   d1= (x**2 + y**2)**0.5  
   distance= (d1**2 + z**2)**0.5   
   return distance      
# End: Calculate distance between two 3D points

# Start: Calculate Manhattan Distance 

Write a function `manhattan_distance(x1, y1, x2, y2)` that takes the coordinates of two points and returns their Manhattan Distance.

def manhattan_distance(x1, y1, x2, y2):
   return  abs(x1-x2)+abs(y1-y2)


# End: Calculate Manhattan Distance 

# Start: Predict the value of Y on the vertical axis
Write a function `predict(m, c, x)` that returns the value of `y` based on the formula:

```
y = m * x + c
```
Here’s what the terms mean:

* `x` is the input (like a point on the horizontal axis).
* `y` is the output (like a point on the vertical axis).
* `m` is the *slope* of the line, which tells us how steep the line is.
* `c` is the *intercept*, or where the line crosses the y-axis.

#### **Arguments:**

* `m` – slope of the line (a number)
* `c` – y-intercept of the line (a number)
* `x` – the x-coordinate (a number)

def predict(m,c,x):
    y = m*x+c
    return y


# End: Predict the value of Y on the vertical axis

# Start: Function to calculate slope and intercept of a line and return as tuple

Write a function `fit(x1, y1, x2, y2)` that returns a tuple `(m, c)` representing the slope and intercept of the line passing through the two points `(x1, y1)` and `(x2, y2)`.

def fit(x1, y1, x2, y2):
    #y = m*x+c
    # y -> point on vertical axis, m -> slope, x -> point on the horizontal axis , 
    #c -> intercept, where the line crosses the y axis
    m = abs((y2-y1)/(x2-x1))
    c = abs(y1- (m*x1))
    return (m,c)

# End: Function to calculate slope and intercept of a line and return as tuple

# Start: Function to calculate derivative

Write a function `approx_derivative(func, x, h)` that:

* Takes a function `func` that accepts a single argument,
* A value `x` where we want to find the derivative,
* And a small number `h` (like `0.0001`),
* Returns the approximate derivative of `func` at `x`.

def approx_derivative(func, x, h):
    derivative = (func(x+h)-func(x))/h
    return derivative
    

# End: Function to calculate derivative
