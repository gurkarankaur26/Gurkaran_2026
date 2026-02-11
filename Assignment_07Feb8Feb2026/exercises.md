
** Loops and Arrays Exercises **
** Rest of the questions are solved in the previous assignments **


Fair Coin Toss

Explanation:
A coin has two sides: Head and Tail. If you flip a fair coin, both sides should have an equal chance of appearing. In programming, we can simulate this randomness using the random module in Python.

The function random.random() generates a random number between 0.0 (inclusive) and 1.0 (exclusive).
If the number is less than 0.5, we can decide it means Head.
If the number is greater than or equal to 0.5, we can decide it means Tail.
In this exercise, you will design a function that:

Simulates a fair coin toss.
Prints "HEAD" if it lands on head, "TAIL" if it lands on tail.
Returns 0 for head and 1 for tail.

Exercise:
Write a function fair_coin_toss() that uses random.random() to simulate a fair coin toss.

If the result is head, print "HEAD" and return 0.
If the result is tail, print "TAIL" and return 1.
Example:
# Example 1: Suppose random.random() gave 0.23 (< 0.5)
fair_coin_toss()  
# Output:
# HEAD
# Returns: 0

# Example 2: Suppose random.random() gave 0.76 (>= 0.5)
fair_coin_toss()  
# Output:
# TAIL
# Returns: 1
Biased Coin Toss
Explanation:
In a fair coin toss, the chance of getting Head or Tail is equal — each has a probability of 50%. But sometimes, we want to design a biased coin where the chances are not equal.

For example, let’s say we want the coin to show Head 70% of the time and Tail 30% of the time. To do this, we can use Python’s random.random() function, which generates a random number between 0 and 1.

If the number is less than 0.7 → we decide it’s a Head.
Otherwise → it’s a Tail.
We will also print the result ("Head" or "Tail") and return 0 for Head and 1 for Tail.

Exercise:
Write a function biased_coin_toss() that simulates a coin toss with 70% chance of Head and 30% chance of Tail.

Use random.random().
Print "Head" if it’s Head and "Tail" if it’s Tail.
Return 0 for Head and 1 for Tail.
Example:
# Example usage (your output may vary because of randomness)

biased_coin_toss()
# Output: Head
# Return: 0

biased_coin_toss()
# Output: Tail
# Return: 1
Biased Coin Toss with Probability Argument
Explanation:
A coin toss doesn’t always need to be fair. We can bias a coin by changing the probability of getting Head.

If the probability of Head is p, then the probability of Tail is 1 - p.
We use Python’s random.random() function, which generates a random number between 0 and 1.
How it works:

If the random number is less than p → it’s a Head.
Otherwise → it’s a Tail.
We will print the result ("Head" or "Tail") and return:

0 for Head
1 for Tail
Exercise:
Write a function biased_coin_toss(p) that simulates a coin toss with probability p for Head.

Use random.random().
Print "Head" if it’s Head and "Tail" if it’s Tail.
Return 0 for Head and 1 for Tail.
Example:
# Example usage (your output may vary because of randomness)

biased_coin_toss(0.7)
# Output: Head
# Return: 0

biased_coin_toss(0.3)
# Output: Tail
# Return: 1
Weighted Choices
Explanation:
Sometimes, we need to select one item out of many, but not all items have the same chance. For example:

Suppose you have three fruits: ["Apple", "Banana", "Cherry"]

You want the chance of picking them to be [0.5, 0.3, 0.2]

Apple → 50% chance
Banana → 30% chance
Cherry → 20% chance
Exercise:
Write a function weighted_choice(probabilities) that:

Takes a list of probabilities (which should sum to 1).
Uses random.random() to select one index based on the given weights.
Returns the index of the chosen element.
Example:
# Example usage (your output may vary because of randomness)

weighted_choice([0.5, 0.3, 0.2])
# Possible Return: 0   (with ~50% chance)
# Possible Return: 1   (with ~30% chance)
# Possible Return: 2   (with ~20% chance)

weighted_choice([0.1, 0.1, 0.8])
# Likely Return: 2   (since 80% chance)
Hint: To implement this, we can use cumulative probability ranges:

Generate a random number r between 0 and 1 using random.random().
See which interval r falls into.
Example with [0.5, 0.3, 0.2]:

If r < 0.5 → pick index 0 (Apple).
If 0.5 <= r < 0.8 → pick index 1 (Banana).
If 0.8 <= r < 1.0 → pick index 2 (Cherry).
The function should return the index of the chosen element.

Normalize a List into Probabilities
Explanation:
Sometimes we have a list of numbers that represent weights or importance, but they don’t add up to 1. To convert them into probabilities, we need to make sure that:

Each number is divided by the total sum of all numbers.
The resulting list always adds up to 1.0.
Example:

Input: [1, 2, 2]
Sum = 1 + 2 + 2 = 5
Divide each element by 5 → [1/5, 2/5, 2/5] = [0.2, 0.4, 0.4]
This is often used in machine learning, probability models, and weighted random choices.

Exercise:
Write a function normalize_to_probabilities(numbers) that:

Takes a list of numbers.
Converts them into probabilities so that their sum is 1.
Returns the new list of probabilities.
Example:
normalize_to_probabilities([1, 2, 2])
# Output: [0.2, 0.4, 0.4]

normalize_to_probabilities([3, 3, 4])
# Output: [0.3, 0.3, 0.4]
Softmax Function
Explanation:
The softmax function is widely used in machine learning, especially in classification tasks. It converts a list of numbers into probabilities, just like normalization, but with an extra twist:

First, take the exponential of each number.
Then, divide each exponential by the sum of all exponentials.
This makes sure:

All outputs are positive.
They add up to 1 (so they can be treated as probabilities).
Example: For numbers [1, 2, 3]:

Exponentials:

exp(1) ≈ 2.718
exp(2) ≈ 7.389
exp(3) ≈ 20.085
Sum = 2.718 + 7.389 + 20.085 = 30.192

Probabilities:

2.718 / 30.192 ≈ 0.09
7.389 / 30.192 ≈ 0.24
20.085 / 30.192 ≈ 0.67
So [1, 2, 3] → [0.09, 0.24, 0.67].

Exercise:
Write a function softmax(values) that:

Takes a list of numbers.
Applies the softmax transformation.
Returns the resulting list of probabilities.
👉 Hint: Use math.exp(x) for exponentials.

Example:
softmax([1, 2, 3])
# Output: [0.09, 0.24, 0.67]  (approx)

softmax([2, 2, 2])
# Output: [0.33, 0.33, 0.33]
Softmax Function (with Numerical Stability)
Explanation:
The softmax function converts a list of numbers into probabilities. It’s used in machine learning to represent the probability distribution of classes.

Formula:

softmax
(
x
i
)
=
e
x
i
∑
j
e
x
j

But there’s a numerical stability problem:

If the numbers are very large (like 1000), exp(1000) will overflow.
👉 Trick: Subtract the maximum value before exponentiation. This doesn’t change the result because softmax only cares about relative differences.

So instead of computing exp(x), we compute:

e
x
i
−
max
(
x
)

This keeps the numbers smaller and avoids overflow.

Exercise:
Write a function softmax(values) that:

Finds the maximum number in the list.
Subtracts this max from every element.
Applies the exponential function.
Divides each exponential by the sum of all exponentials.
Returns the probabilities as a list.
Example:
softmax([1, 2, 3])
# Output: [0.09, 0.24, 0.67]  (approx)

softmax([1000, 1001, 1002])
# Output: [0.09, 0.24, 0.67]  (approx, stable!)

Temperature Scaling
Explanation:
In machine learning, we sometimes want to control how confident or uncertain our probability distribution is. That’s where the temperature parameter (T) comes in.

We modify the softmax formula:

softmax
(
x
i
,
T
)
=
e
x
i
/
T
∑
j
e
x
j
/
T

If T = 1 → normal softmax.
If T < 1 → the distribution becomes sharper (higher confidence, one class dominates).
If T > 1 → the distribution becomes flatter (more uncertainty, probabilities spread out).
Example with values [1, 2, 3]:

T = 1 → [0.09, 0.24, 0.67]
T = 0.5 → [0.02, 0.12, 0.86] (sharper)
T = 2 → [0.21, 0.31, 0.48] (flatter)
We should also use the numerical stability trick (subtract the max).

Exercise:
Write a function softmax_with_temperature(values, T) that:

Divides each number by T.
Subtracts the max value for stability.
Applies the exponential function.
Normalizes by dividing each exponential by the sum.
Returns the probability distribution.

Example:
softmax_with_temperature([1, 2, 3], 1)
# Output: [0.09, 0.24, 0.67]

softmax_with_temperature([1, 2, 3], 0.5)
# Output: [0.02, 0.12, 0.86]  (sharper)

softmax_with_temperature([1, 2, 3], 2)
# Output: [0.21, 0.31, 0.48]  (flatter)


Weighted Choices with Temperature

Explanation
You often need to pick one item from a list where each item has a weight (importance). Higher weight ⇒ higher chance to be chosen. Temperature (T) lets you control how sharp or flat those chances are:

T < 1 → Sharper distribution (the biggest weights dominate more).
T = 1 → Original weighting.
T > 1 → Flatter distribution (even small weights get more chance).
A simple way to add temperature to positive weights is:

Transform each weight as 
w
i
,
1
/
T
.
Normalize the transformed weights so they sum to 1 (convert to probabilities).
Sample an index using these probabilities.
This behaves like softmax with temperature on logits, but works directly on positive weights.

Exercise
Write a function weighted_choice_with_temperature(weights, T) that:

Arguments

weights: a list of non-negative numbers (at least one must be > 0).
T: a positive float (temperature).
Behavior

Apply temperature scaling: scaled = [w ** (1.0 / T) for w in weights].
Convert scaled to probabilities by dividing each by their sum.
Draw a single index according to these probabilities using a single random number (random.random()), by walking cumulative sums.
Return the selected index (an int).
Notes / Constraints

If T <= 0, you may raise a ValueError.
If all weights are zero, you may raise a ValueError.
Use only the standard library (random and basic Python).
Example
# Example usage (outputs are stochastic; comments show likely behavior)

# Heavily favors index 2 at lower T, but evens out at higher T
weighted_choice_with_temperature([1, 2, 8], T=0.5)  # Likely returns 2 most of the time
weighted_choice_with_temperature([1, 2, 8], T=1.0)  # Still favors 2, but less sharply
weighted_choice_with_temperature([1, 2, 8], T=2.0)  # Flatter; 0 and 1 get picked more often

# Equal weights stay equal at any T
weighted_choice_with_temperature([3, 3, 3], T=0.3)  # ~uniform over {0,1,2}
weighted_choice_with_temperature([3, 3, 3], T=2.0)  # ~uniform over {0,1,2}

Flatten an Array

Explanation:
Sometimes, lists (or arrays) in Python are not just simple lists of numbers but contain other lists inside them. Such lists are called nested lists. For example: [1, [2, 3], [4, [5, 6]]]

To make it easier to work with, we might want to flatten the list—meaning we turn it into a single list with no nesting: [1, 2, 3, 4, 5, 6].

A powerful way to solve this problem is by using recursion. Recursion means a function calls itself to solve a smaller version of the problem. In this case:

If the element is a number, just add it to the result.
If the element is a list, flatten that list (by calling the function again) and add its elements.


Exercise:
Write a function flatten_list(nested_list) that takes a possibly nested list of numbers and returns a flat list (all elements in a single list).

💡 Hint: Use recursion. When you see another list inside, call flatten_list again.

Example:
flatten_list([1, [1, 2, [3, 4]]])  
# Output: [1, 1, 2, 3, 4]

flatten_list([1, [2, [3, [4, 5]]]])  
# Output: [1, 2, 3, 4, 5]


Solve Expression (Array Form)

Explanation:
In some problems, instead of writing math expressions like "(20 + 40) * 90", the expression is stored in a special way: as arrays (lists) of three elements.

The first element is an operator (+, -, *, /).

The second and third elements are the operands.

An operand can be:

a number, like 20, or
another nested array, which is itself an expression.
For example:

["*", ["+", 20, 40], 90]

This means:

First solve ["+", 20, 40] → 60
Then solve ["*", 60, 90] → 5400
So, the result is 5400.

To solve this, you can use recursion:

If the input is just a number, return it.
Otherwise, solve the left operand, solve the right operand, then apply the operator.

Exercise:
Write a function solve_expression(expr) that takes an expression (in this special array format) and returns its value.

💡 Hint: Use recursion to handle nested expressions.

Example:
solve_expression(["*", ["+", 20, 40], 90])  
# Output: 5400

solve_expression(["-", ["*", ["/" 100 10], 5], 15])  
# Output: 35   (because ((100/10)*5) - 15 = 50 - 15)

Write a function to print all the permutations of a string containing uinque letters
example input: pr output: pr rp input pri output: pri pir rpi rip ipr irp



#**********************************************************************************************#
   ## Start: Dictionary exercises
#**********************************************************************************************#

## Word Count Using Dictionary

### Explanation:

When you have a huge block of text, sometimes you want to know how many times each word appears. For example, in a book or an article, some words occur many times (like *the*, *and*), while others occur only once.

We can solve this problem by using a **dictionary** in Python:

* The *keys* of the dictionary will be the words.
* The *values* will be how many times each word appears in the text.

For example, in the text `"hello world hello"`,
the dictionary would look like:
`{"hello": 2, "world": 1}`

This is called a **word count**.

### Exercise:

Write a function `word_count(text)` that:

* Takes a string `text` as input.
* Splits the text into words (you can use `split()`).
* Counts how many times each word appears using a dictionary.
* Returns the dictionary of word counts.

💡 **Hint**: You can test your function using the large file provided:

```python
txt = open('/cxldata/big.txt').read()
```

### Example:

```python
word_count("hello world hello")
# Output: {'hello': 2, 'world': 1}

word_count("apple orange apple banana orange")
# Output: {'apple': 2, 'orange': 2, 'banana': 1}
```
---

## Find Anagrams in a Text

### Explanation:

An **anagram** is a word formed by rearranging the letters of another word.
For example:

* `"listen"` and `"silent"` are anagrams.
* `"evil"` and `"vile"` are also anagrams.

To find anagrams in a large text, one useful trick is to use a **dictionary (hash map)**:

* We can sort the letters of each word to form a *key*.

  * Example: `"listen"` → `"eilnst"`, `"silent"` → `"eilnst"`.
* All words that share the same sorted key are anagrams of each other.
* We group words together in the dictionary using these keys.

This method is very efficient, even for huge texts.

---

### Exercise:

Write a function `find_anagrams(text)` that:

1. Splits the given text into words.
2. Uses a dictionary to group words that are anagrams of each other.
3. Returns a dictionary where:

   * The key is the sorted letters (like `"eilnst"`).
   * The value is a list of words that are anagrams.

You can test your function using a big text file:

```python
txt = open('/cxldata/big.txt').read()
```

---

### Example:

```python
find_anagrams("listen silent enlist inlets hello world")
# Possible Output:
# {
#   'eilnst': ['listen', 'silent', 'enlist', 'inlets'],
#   'ehllo': ['hello'],
#   'dlorw': ['world']
# }
```

```python
find_anagrams("evil vile live veil")
# Output:
# {
#   'eilv': ['evil', 'vile', 'live', 'veil']
# }
```

---
## Build an Expense Tracker

### Explanation:

When you spend money, you usually want to keep track of **where the money is going**. For example, you might spend on *food*, *rent*, *travel*, and so on. An **expense tracker** helps you organize your spending by category (also called *expense head*).

We can build a simple tracker using a **dictionary**:

* The *keys* will be the expense heads (like `"food"`, `"rent"`, `"travel"`).
* The *values* will be the total amount spent under that head.

We will write **two functions**:

1. `update_expenses(expense_list, expenses_dict)` → updates the dictionary with new expenses.

   * `expense_list` is a list of tuples like `[("food", 200), ("rent", 1000)]`.
   * `expenses_dict` is the dictionary where totals are stored.

2. `print_expenses(expenses_dict)` → prints the overall expenses under each head in a clean way.

---

### Exercise:

Write the following functions:

```python
def update_expenses(expense_list, expenses_dict):
    """
    Updates the dictionary with expenses from the list.
    Each element of expense_list is a tuple: (expense_head, amount).
    If the head already exists, add to its total.
    Otherwise, create a new entry.
    """
    pass


def print_expenses(expenses_dict):
    """
    Prints all expense heads and their total amounts.
    Example format:
    food : 500
    rent : 1000
    """
    pass
```

---

### Example Usage:

```python
expenses = {}

update_expenses([("food", 200), ("rent", 1000)], expenses)
update_expenses([("food", 300), ("travel", 150)], expenses)

print_expenses(expenses)
```

**Expected Output:**

```
food : 500
rent : 1000
travel : 150 ```

---

#**********************************************************************************************#
   ## End: Dictionary exercises
#**********************************************************************************************#