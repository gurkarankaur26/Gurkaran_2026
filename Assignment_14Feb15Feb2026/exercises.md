Object and Classes

Create a LineModel Class with a function fit and predict.

Create a vector Class with the operations Add, Multiply,Distance, Turn

Turn :  Q: Someone is moving with a velocity v (vector e.g. (3,4)). And the vector is turned by an angle theta counter clockwise.# The speed remains same. What's new velocity? See if you can add a new function in vector class 'turn(theta_ccw)'

############## Binary Search #####################
##################################################

Binary Search
Find Square Root using Binary Search
Explanation:
The square root of a number is a value that, when multiplied by itself, gives the original number. For example, the square root of 25 is 5 because 
5
×
5
=
25
5×5=25.

Instead of using built-in functions like math.sqrt, we can use a technique called binary search to approximate the square root. The idea is simple:

Suppose we want the square root of n.

We know the answer will be between 0 and n (if n >= 1).

We repeatedly check the middle of the current range:

If mid * mid is close to n, then mid is our answer.
If mid * mid is too small, we move to the right half.
If mid * mid is too large, we move to the left half.
We continue until the approximation is good enough.

This method is efficient because it cuts the search space in half each time.

Exercise:
Write a function sqrt_binary_search(n, precision) that returns the square root of n up to the given decimal precision.

n → the number whose square root we want.
precision → how close we want the answer to be (for example, 0.0001).
Example:
sqrt_binary_search(25, 0.0001)   # Output: approximately 5.0
sqrt_binary_search(2, 0.0001)    # Output: approximately 1.4142
Perfect! Let’s build the same kind of structured exercise for Cube Root.

Compute Cube Root using Binary Search
Explanation (simple)
The cube root of a number n is a value x such that:

x
×
x
×
x
=
n
x×x×x=n

For example:

Cube root of 27 is 3 (since 
3
×
3
×
3
=
27
3×3×3=27)
Cube root of 8 is 2.
Instead of using n ** (1/3) or math.pow(n, 1/3), we can approximate the cube root using binary search. The idea is similar to finding a square root:

Choose a search range where the cube root must lie.
Repeatedly check the midpoint.
Narrow down the range until we are close enough.
Exercise
Write a function cuberoot_binary_search(n, precision) that returns the cube root of n up to the given precision.

Arguments:

n: number (can be positive, negative, or zero).
precision: small positive float (like 1e-6).
Return:

Approximate cube root of n as a float.
Step-by-Step Hints
Hint 1 — Handle simple cases

If n == 0, return 0.
If n == 1, return 1.
If n == -1, return -1.
Hint 2 — Handle negatives

The cube root of a negative number is also negative (e.g., cube root of -8 is -2).
You can take the cube root of |n| (absolute value) and then negate the result.
Hint 3 — Initial search range

If |n| >= 1, the cube root lies in [0, |n|].
If |n| < 1, the cube root lies in [0, 1].
Hint 4 — Midpoint and test

Compute mid = (low + high)/2.
Compute cube = mid*mid*mid.
Compare cube with |n|.
Hint 5 — Update range

If cube < |n|, move low = mid.
Else move high = mid.
Hint 6 — Stopping condition Stop when abs(cube - |n|) <= precision.

Hint 7 — Return value

If n was negative, return -mid.
Otherwise return mid.
Example Usage
cuberoot_binary_search(27, 1e-6)   # ≈ 3.0
cuberoot_binary_search(8, 1e-6)    # ≈ 2.0
cuberoot_binary_search(-64, 1e-6)  # ≈ -4.0
cuberoot_binary_search(0.001, 1e-6) # ≈ 0.1
Compute nth Root
Explanation:
The nth root of a number is a value that, when multiplied by itself n times, gives back the original number.

For example:

The square root (2nd root) of 16 is 4, because 
4
×
4
=
16
4×4=16.
The cube root (3rd root) of 27 is 3, because 
3
×
3
×
3
=
27
3×3×3=27.
In general, the nth root of a number x is written as:

x
n
=
x
1
/
n
n
  
x
​
 =x 
1/n
 

For example:

81
1
/
4
=
3
81 
1/4
 =3, because 
3
×
3
×
3
×
3
=
81
3×3×3×3=81.
32
1
/
5
=
2
32 
1/5
 =2, because 
2
×
2
×
2
×
2
×
2
=
32
2×2×2×2×2=32.
Exercise:
Write a function compute_nth_root(x, n) that takes two numbers:

x → the number you want to find the root of
n → the degree of the root
The function should return the nth root of x.

Example:
compute_nth_root(16, 2)   # Output: 4.0  
compute_nth_root(27, 3)   # Output: 3.0  
compute_nth_root(81, 4)   # Output: 3.0  
Here’s a well-structured Python exercise for Compute the Log base 10 using Binary Search, in the same style as your “Compute Interest” example.

Compute log₁₀(x) with Binary Search
Explanation:
The base-10 logarithm of a positive number 
x
x, written 
log
⁡
10
(
x
)
log 
10
​
 (x), is the exponent 
y
y such that:

10
y
=
x
10 
y
 =x

Examples:

log
⁡
10
(
100
)
=
2
log 
10
​
 (100)=2 because 
10
2
=
100
10 
2
 =100.
log
⁡
10
(
0.01
)
=
−
2
log 
10
​
 (0.01)=−2 because 
10
−
2
=
0.01
10 
−2
 =0.01.
Idea: Instead of using built-in math.log10, we can binary search for the exponent 
y
y so that 
10
y
10 
y
  gets as close as possible to 
x
x. Why binary search works: the function 
f
(
y
)
=
10
y
f(y)=10 
y
  is strictly increasing, so we can keep a low/high range for 
y
y and narrow it down until 
10
y
10 
y
  is very close to 
x
x.

Key points:

Only defined for x > 0.
If 
x
=
1
x=1, the answer is 0.
If 
0
<
x
<
1
0<x<1, the result is negative.
We’ll stop when the answer is precise within a small tolerance (like 1e-7).
Exercise:
Write a function log10_binary_search(x, tol=1e-7) that returns an approximation of 
log
⁡
10
(
x
)
log 
10
​
 (x).

Requirements:

Parameters:

x (float): the positive number whose base-10 log you want.
tol (float): desired precision for the result (default 1e-7).
Returns:

A float approximating 
log
⁡
10
(
x
)
log 
10
​
 (x) such that abs(10**ans - x) <= tol * max(1, x).
Behavior:

Raise a ValueError if x <= 0.

Use binary search on the exponent y, not on x.

First, find a bracketing range [low, high] such that 10**low <= x <= 10**high.

If x >= 1, you can start with low = 0, high = 1 and keep doubling high until 10**high >= x.
If x < 1, start with low = -1, high = 0 and keep doubling the magnitude of low (e.g., low *= 2) until 10**low <= x.
Then binary search within [low, high]:

Let mid = (low + high) / 2.
If 10**mid is less than x, move low = mid; else move high = mid.
Stop when high - low is small enough (e.g., < 1e-12) or when the forward check abs(10**mid - x) meets the tolerance.
Example:
log10_binary_search(100)           # Output: 2.0
log10_binary_search(1000)          # Output: 3.0
log10_binary_search(0.01)          # Output: -2.0
round(log10_binary_search(2), 5)   # Output: 0.30103  (approximately)
Hints / Checkpoints:
Guardrails: If x <= 0, raise ValueError. If x == 1, return 0.0.

Bracket the answer:

f(y) = 10**y. You need low and high such that f(low) <= x <= f(high).
Expand outward by doubling the interval on the side that doesn’t yet contain x.
Binary search loop:

Compute mid; evaluate f(mid).
If f(mid) < x, move low = mid; else high = mid.
Stopping rule:

Either abs(10**mid - x) <= tol * max(1, x) OR the interval high - low is tiny (like < 1e-12).
Return: mid (or the midpoint of the final [low, high]).

Compute logₙ(x) with Binary Search
Explanation:
The logarithm of a positive number 
x
x with base 
n
n (where 
n
>
0
n>0 and 
n
≠
1
n

=1) is the exponent 
y
y such that:

n
y
=
x
n 
y
 =x

Examples:

log
⁡
2
(
8
)
=
3
log 
2
​
 (8)=3 because 
2
3
=
8
2 
3
 =8.
log
⁡
3
(
81
)
=
4
log 
3
​
 (81)=4 because 
3
4
=
81
3 
4
 =81.
log
⁡
5
(
0.04
)
=
−
2
log 
5
​
 (0.04)=−2 because 
5
−
2
=
0.04
5 
−2
 =0.04.
Instead of using Python’s built-in math.log(x, n), we can use binary search on the exponent 
y
y to find the answer. Why? Because the function 
f
(
y
)
=
n
y
f(y)=n 
y
  is strictly increasing (when 
n
>
1
n>1) or strictly decreasing (when 
0
<
n
<
1
0<n<1), so binary search will always converge to the correct solution.

Exercise:
Write a function log_base_n(x, n, tol=1e-7) that returns an approximation of 
log
⁡
n
(
x
)
log 
n
​
 (x).

Requirements:

Parameters:

x (float): the number whose log you want. Must be > 0.
n (float): the base of the logarithm. Must be > 0 and not equal to 1.
tol (float): the precision of the answer (default 1e-7).
Returns:

A float approximating 
log
⁡
n
(
x
)
log 
n
​
 (x).
Behavior:

Raise ValueError if x <= 0 or if n <= 0 or n == 1.

Use binary search on exponent y:

Find [low, high] such that n**low <= x <= n**high (or vice versa if 0 < n < 1).
Repeatedly narrow down the range until n**mid is close enough to x.
Example:
log_base_n(8, 2)      # Output: 3.0
log_base_n(81, 3)     # Output: 4.0
log_base_n(0.04, 5)   # Output: -2.0
round(log_base_n(10, 2), 5)   # Output: 3.32193 (approximately)
Hints / Checkpoints:
Guardrails:

If x <= 0, raise ValueError.
If n <= 0 or n == 1, raise ValueError.
If x == 1, return 0.0.
Bracketing the answer:

If n > 1:

Start with [0, 1] and keep doubling high until n**high >= x.
If x < 1, go negative: [−1, 0], doubling low downward until n**low <= x.
If 0 < n < 1:

The function decreases, so inequalities flip — but the idea is the same.
Binary search:

Compute mid = (low + high) / 2.
If n**mid is too small/large compared to x, adjust the interval.
Stopping condition:

Stop when abs(n**mid - x) <= tol * max(1, x) or interval width < 1e-12.
At what value of x this has minimum value: x^4 - 3*x^3 - 5x + 10
Open ended question
Differentiation
Plot the curve

