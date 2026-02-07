
# Note: Rest of the questions for Expressions/Functions and If else were answered in the previous assignment-Assignment_11Jan2026 in git hub


## Extract last digit from a number

## Remove the last digit from a number

### **Exercise:**

Write a function `fit(x1, y1, x2, y2)` that returns a tuple `(m, c)` representing the slope and intercept of the line passing through the two points `(x1, y1)` and `(x2, y2)`.

### **Exercise:**

Write a function `approx_derivative(func, x, h)` that:

* Takes a function `func` that accepts a single argument,
* A value `x` where we want to find the derivative,
* And a small number `h` (like `0.0001`),
* Returns the approximate derivative of `func` at `x`.

## Print a random integer between 1 and 6
You have a random.random() that prints a decimal number.

Write a function `my_impurity(c1, c2)` that calculates the impurity of a set containing two classes:

* `c1` is the number of examples from **class 1**
* `c2` is the number of examples from **class 2**

You should **devise your own formula** to calculate impurity. Your formula must meet these conditions:

1. If all items are from one class (`c1 = 0` or `c2 = 0`), impurity should be `0`.
2. The impurity should increase as the classes become more evenly balanced.
3. The impurity should be **maximum** when `c1 == c2`.

You may use arithmetic operators like `+`, `-`, `*`, `/`, and functions like `abs()` if needed.

