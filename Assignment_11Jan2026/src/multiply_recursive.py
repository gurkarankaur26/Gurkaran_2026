def multiply_recursive(a, b):
    # Base case
    if b == 0:
        return 0

    # If b is negative
    if b < 0:
        return -multiply_recursive(a, -b)

    # Recursive case
    return a + multiply_recursive(a, b - 1)
