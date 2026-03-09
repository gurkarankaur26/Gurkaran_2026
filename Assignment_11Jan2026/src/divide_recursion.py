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