# Loops and Arrays exercises

 Write a function `find_min_max(numbers)` that takes a list of numbers as input and 
 returns a tuple `(minimum, maximum)`.


Write a function `min_max_normalize(value, data)` that:

* Takes two inputs:

  * `value`: the number you want to normalize
  * `data`: a list of numbers (dataset)
* Returns the normalized value of `value` using min-max normalization.


Write a function `compute_sd(numbers)` that takes a list of numbers and returns the standard deviation.

Write a function `find_outliers(nums, threshold)` that returns a list of numbers from `nums` that are outliers based on the given z-score threshold.

**Arguments:**

* `nums`: a list of numbers
* `threshold`: a number (like 2 or 3) representing how far from the mean we consider values as outliers

Write a function `compute_iqr(data)` that takes a list of numbers and returns the IQR.

Write a function `standardize(data)` that takes a list of numbers and returns a new list where each number is standardized.

Write a function `compute_rmse(actual, predicted)` that:

* Takes two lists of equal length: `actual` and `predicted`.
* Returns the Root Mean Square Error between them.


Write a function `compute_mae(actual, predicted)` that:

* Takes two lists of points (each point is a list of numbers, e.g. `[x, y, z, ...]`).
* Returns the mean absolute error across all dimensions.

 Write a function `compute_huber_loss(y_true, y_pred, delta)` that takes:

* `y_true`: a list of actual values
* `y_pred`: a list of predicted values
* `delta`: the threshold value

and returns the **average Huber loss**.


Write a function `closer_point(P, A, B)` that:

* Takes three points (`P`, `A`, and `B`) as lists of numbers (same length).
* Returns `"A"` if P is closer to A, `"B"` if P is closer to B, or `"Equal"` if the distances are the same.


Write a function `find_nearest_neighbour(numbers, target)` that returns the nearest neighbour of the target from the list.



Write a function `find_nearest_neighbour(points, target)` that returns the point from the list `points` which is closest to the `target`.

* `points` is a list of `(x, y)` tuples.
* `target` is a tuple `(x, y)` representing the location we want to compare.
* The function should return the nearest neighbour point as a tuple.


Write a function `find_nearest_neighbour(point, points)` that takes:

* `point`: a list of numbers representing coordinates of a point in N-dimensions
* `points`: a list of points (each a list of numbers)

and returns the point from `points` that is nearest to `point`

Write a function `multiply_polynomial(poly, num)` that takes:

* `poly`: a list of coefficients of the polynomial
* `num`: a number to multiply the polynomial with

The function should return a new list of coefficients after multiplication.


Write a function `add_polynomials(p1, p2)` that takes two lists `p1` and `p2`, representing two polynomials, and returns a new list with their sum.


Write a function multiply_polynomials(p1, p2) that takes two lists of coefficients p1 and p2, and returns a new list representing their product.


Write a function solve_for_first_variable(equation, vars) that returns the value of the first variable.

equation: a list of numbers where the first 
n
n elements are coefficients of the variables and the last element is the right-hand side value.
vars: a list of values for the last 
n
−
1
n−1 variables.


