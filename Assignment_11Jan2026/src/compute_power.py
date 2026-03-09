def compute_power(x, n):
     if n==0:
       return 1
     if n==1:
       return x
     if n > 0:
        return x*compute_power(x,n-1)
     if n < 0:
       return (1/ (x * compute_power(x,abs(n)-1)))
    