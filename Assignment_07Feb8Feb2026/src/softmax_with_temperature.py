   
'''Write a function softmax_with_temperature(values, T) that:

Divides each number by T. Subtracts the max value for stability. 
Applies the exponential function. 
Normalizes by dividing each exponential by the sum. Returns the probability distribution.'''  
    
    
import math
def  softmax_with_temperature(lst,T):
    if T <= 0:
        raise ValueError("Temperature must be positive")
    sofmax_normalised_list=[]
    exp_total=0
    len_lst = len(lst)
    max_val = max(lst)/T
    for i,ele in enumerate(lst):
        exp_total = exp_total + math.exp((ele/T)-max_val)
    for i in range(len_lst):
        val1 = math.exp((lst[i]/T)-max_val)
        val2 =val1/exp_total
        sofmax_normalised_list.append(round(val2,2))
    return sofmax_normalised_list