def power(x,n):
    if x<0 or n<0:
        print('Provide a positive value for x and n')
        return 
    if n==0:
       return 1
    if n==1:
       return x

    return x * power(x,n-1)