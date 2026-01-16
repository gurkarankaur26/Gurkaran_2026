Write a function `factorial_recursive(n)` that takes one argument `n` (a non-negative integer) and returns the factorial of that number using recursion.

If `n` is 0, the function should return 1.

### Start: Function to calculate factorial of a number through recursion

def factorial_recursive(n):
    if n< 0:
        print('Provide a non negative number')
        return
    if n == 1:
        return 1
    else:
        return n * factorial_recursive(n-1)

### End: Function to calculate factorial of a number through recursion

### Start: Function to multiply recursive 

Write a function `multiply_recursive(a, b)` that multiplies two integers using recursion (without using the `*` operator).

* `a`: the first number (int)
* `b`: the second number (int)

Return the product of `a` and `b`.

def multiply_recursive(a, b):
    # Base case
    if b == 0:
        return 0

    # If b is negative
    if b < 0:
        return -multiply_recursive(a, -b)

    # if b is positive
    return a + multiply_recursive(a, b - 1)


### End: Function to multiply recursive 

### Start: Function to calculate power using recursion

Write a function `power(x, n)` that uses recursion to return $x^n$, where `n` is a positive integer.

def power(x,n):
    if x<0 or n<0:
        print('Provide a positive value for x and n')
        return 
    if n==0:
       return 1
    if n==1:
       return x
    return x * power(x,n-1)

### End: Function to calculate power using recursion

### Start: Function to calculate power using recursion Handle positive, negative, and zero values of power

Write a function `compute_power(x, n)` that returns $x^n$ using recursion. Handle positive, negative, and zero values of $n$.

def compute_power(x, n):
     if n==0:
       return 1
     if n==1:
       return x
     if n > 0:
        return x*compute_power(x,n-1)
     if n < 0:
       return (1/ (x * compute_power(x,abs(n)-1)))

### End: Function to calculate power using recursion Handle positive, negative, and zero values of power

### Start: Function to find quotient and remainder by dividing the dividend by divisor

Write a function `recursive_divide(dividend, divisor)` that returns a tuple `(quotient, remainder)` using recursion.
You **must not** use the `//` or `%` operators.

* `dividend`: a non-negative integer
* `divisor`: a positive integer

**Return:** A tuple of two integers: `(quotient, remainder)`
def recursive_divide(dividend, divisor,count=0):
    if(str(dividend).isdigit()==False or  str(divisor).isdigit()==False):
        print('Provide postive numeric values for dividend and divisor')
        return      
    if dividend <0 or divisor < 0:
        print('Provide postive numeric values for dividend and divisor')
        return      
    dividend = dividend - divisor    
    if dividend < divisor: 
        result = (count+1,dividend)
        return (result)       
    return recursive_divide(dividend,divisor,count+1)

### End: Function to find quotient and remainder by dividing the dividend by divisor

### Start: Function to find the HCF of two numbers using Euclid's method

Write a function named `compute_hcf(a, b)` that takes two positive integers `a` and `b` and returns their HCF using Euclid's method with recursion.

* You should **use recursion** to solve this problem.
* The function should return an integer.

def compute_hcf(a, b):
     if(str(a).isdigit()==False or  str(b).isdigit()==False):
        print('Provide postive numeric values to find HCF')
        return      
     if a <0 or b < 0:
        print('Provide postive numeric values to find HCF')
        return    
     if b==0:
        return a
     remainder = a%b
     a=b
     b=remainder
     return compute_hcf(a,b)


### End: Function to find the HCF of two numbers using Euclid's method

### Start: Function for Tower of Hanoi using recursion

Write a function `solve_hanoi(n, source='A', auxiliary='B', target='C')` that:

* Prints each move exactly in the format: `Moving <disc> from <source> to <target>.`
* Uses recursion: base case `n == 1`, recursive case for `n > 1` using the general rule above.
* Returns the **total number of moves** performed.

def solve_hanoi(n, source='A', auxiliary='B', target='C'):
    if n == 1:
        print(f"Moving disk 1 from {source} to {target}")
        return 1

    moves = 0
    moves += solve_hanoi(n-1, source, target, auxiliary)
    print(f"Moving disk {n} from {source} to {target}")
    moves += 1
    moves += solve_hanoi(n-1, auxiliary, source, target)

    return moves

### End: Function for Tower of Hanoi using recrsion