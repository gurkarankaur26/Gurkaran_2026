       
'''Write a function normalize_to_probabilities(numbers) that:
   Takes a list of numbers. Converts them into probabilities so that their sum is 1.
   Returns the new list of probabilities. Example: normalize_to_probabilities([1, 2, 2])'''

def normalize_to_probabilities(lst):
    normalised_list=[]
    total=0
    len_lst = len(lst)
    for i,ele in enumerate(lst):
        total = total + ele
    if total != 1:
       for i in range(len_lst):
            normalised_list.append(lst[i]/total)            
       return normalised_list
    else:
        return ('List is already normalised')