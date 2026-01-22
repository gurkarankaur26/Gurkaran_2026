
# Note: Rest of the questions for Expressions/Functions and If else were answered in the previous assignment-Assignment_11Jan2026 in git hub


## Extract last digit from a number

def get_last_digit(num):
    return num%10

## Remove the last digit from a number

def remove_last_digit(num):
    return num//10

### **Exercise:**

Write a function `fit(x1, y1, x2, y2)` that returns a tuple `(m, c)` representing the slope and intercept of the line passing through the two points `(x1, y1)` and `(x2, y2)`.

## Start : Function to return slope and intercept
def fit(x1,y1,x2,y2):
    # equation of line with points y = mx +c   
    m:any
    c:any 
    #y1 = m*x1 + c
    #y2 = m*x2 + c
    #y1 -y2 = m*x1 - m*x2 
    #y1-y2 = m(x1-x2)
    m = abs((y1-y2)/(x1-x2))
    # y1 = (abs((y1-y2)/(x1-x2)))*x1 + c
    c = abs(y1 - m*x1)
    return(m,c)
## End : Function to return slope and intercept



### **Exercise:**

Write a function `approx_derivative(func, x, h)` that:

* Takes a function `func` that accepts a single argument,
* A value `x` where we want to find the derivative,
* And a small number `h` (like `0.0001`),
* Returns the approximate derivative of `func` at `x`.

## Start: Function to calculate Derivative
def approx_derivative(func, x, h):
    #h is the small change
    x1= x
    x2=x+h
    y1 = func(x)
    y2 = func(x+h)
    rate_of_change =  abs((y2-y1))/abs(x2-x1)
    return rate_of_change   
## End: Function to calculate Derivative

## Print a random integer between 1 and 6
You have a random.random() that prints a decimal number.

## Start:Function to print random number beween two numbers

def print_random_no(start,end):    
    rno =random.random() # generates random number between 0-1
    num= int(rno*end)
    if num < start:
        print(num+start)
    else:
        print(num)
## End:Function to print random number beween two numbers  

## Start: Function to print Head or Tail

def toss_coin():
    rno = random.random() #random no between 0 and 1
    mid = 1/2
    if rno < mid:
        print('Head')
    else:
        print('Tail')
## End: Function to print Head or Tail

Write a function `my_impurity(c1, c2)` that calculates the impurity of a set containing two classes:

* `c1` is the number of examples from **class 1**
* `c2` is the number of examples from **class 2**

You should **devise your own formula** to calculate impurity. Your formula must meet these conditions:

1. If all items are from one class (`c1 = 0` or `c2 = 0`), impurity should be `0`.
2. The impurity should increase as the classes become more evenly balanced.
3. The impurity should be **maximum** when `c1 == c2`.

You may use arithmetic operators like `+`, `-`, `*`, `/`, and functions like `abs()` if needed.

## Start: Function to calculate impurity

def my_impurity(c1, c2):      
    impurity_value = round((c2*c1)/(c1+c2)/10,2)
    print ('Impurity between '+ str(c1) + ' and '+ str(c2)+': '+str(impurity_value))
        
## End: Function to calculate impurity

