
'''Write a function softmax(values) that:
Takes a list of numbers. Applies the softmax transformation.
Returns the resulting list of probabilities. 👉 Hint: Use math.exp(x) for exponentials.'''

import math
def softmax(lst):
    sofmax_normalised_list=[]
    total=0
    len_lst = len(lst)
    for i,ele in enumerate(lst):
        total = total + math.exp(ele)
    for i in range(len_lst):
        sofmax_normalised_list.append(math.exp(lst[i])/total)
    return sofmax_normalised_list