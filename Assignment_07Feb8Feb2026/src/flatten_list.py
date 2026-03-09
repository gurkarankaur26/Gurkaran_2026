     
''' Write a function flatten_list(nested_list) that takes a possibly nested list of numbers and returns a flat list (all elements in a single list).

💡 Hint: Use recursion. When you see another list inside, call flatten_list again.'''

def flatten_list(lst,result=None): 
    if result == None:
        result =[]
    #print(lst)
    for  ele in lst:
        if isinstance(ele, list): 
            flatten_list(ele,result)
        else:
            result.append(ele)
    return result