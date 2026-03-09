def factorial_recursive(n):
    if n< 0:
        print('Provide a non negative number')
        return
    if n == 1:
        return 1
    else:
        return n * factorial_recursive(n-1)