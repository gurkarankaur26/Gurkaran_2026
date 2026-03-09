
'''Write a function softmax(values) that:
Finds the maximum number in the list. Subtracts this max from every element. 
Applies the exponential function. Divides each exponential by the sum of all exponentials. 
Returns the probabilities as a list. Example: softmax([1, 2, 3])'''

import math
def softmax_xi(lst):
    sofmax_normalised_list=[]
    total=0
    len_lst = len(lst)
    max_val = max(lst)
    print(max_val)
    for i,ele in enumerate(lst):
        total = total + math.exp(ele-max_val)
    for i in range(len_lst):
        sofmax_normalised_list.append(math.exp(lst[i]-max_val)/total)
    return sofmax_normalised_list