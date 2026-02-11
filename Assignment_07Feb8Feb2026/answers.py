

'''Write a function fair_coin_toss() that uses random.random() to simulate a fair coin toss.

If the result is head, print "HEAD" and return 0.
If the result is tail, print "TAIL" and return 1.'''

import random
def fair_coin_toss():
    rnd = random.random()
    #print (rnd)
    if rnd <0.5:
        print('HEAD')
        return 0
    elif rnd >=0.5:
        print('TAIL')
        return 1


'''Write a function biased_coin_toss() that simulates a coin toss with 70% chance of Head and 30% chance of Tail.'''

import random
def biased_coin_toss():
    rnd = random.random()
    #print (rnd)
    if rnd <0.7:
        print('HEAD')
        return 0
    else:
        print('TAIL')
        return 1
    
'''Write a function weighted_choice(probabilities) that:

Takes a list of probabilities (which should sum to 1).
Uses random.random() to select one index based on the given weights.
Returns the index of the chosen element.

Outcome	Probability	Cumulative  Range
0	    0.2	        0.2(0.0+0.2) 0.0. -0.2
1	    0.5	        0.7(0.2+0.5) 0.2  -0.7
2	    0.3	        1.0(0.7+1.0) 0.7  -1.0
'''
import random
def weighted_choice(lst):
    if len(lst) == 1:
        return 0
    rnd = random.random()
    print (rnd)
    cummulative=0
    for i,j in enumerate(lst):  
        #print(rnd,cummulative,j)   
        cummulative = cummulative + j      
        if rnd<=cummulative: 
            #print( i)
            break
        
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

'''Write a function weighted_choice_with_temperature(weights, T) that:
Arguments
weights: a list of non-negative numbers (at least one must be > 0). 
T: a positive float (temperature). 
Behavior:Apply temperature scaling: scaled = [w ** (1.0 / T) for w in weights].
Convert scaled to probabilities by dividing each by their sum. 
Draw a single index according to these probabilities using a single random number (random.random()), by walking cumulative sums. Return the selected index (an int). Notes / Constraints
If T <= 0, you may raise a ValueError. If all weights are zero, you may raise a ValueError.
Use only the standard library (random and basic Python).'''

def weighted_choice_with_temperature(lst,T):
    if T<=0: raise ValueError('T must be postive')
    cntZero=0
    for i,ele in enumerate(lst):
        if ele == 0: cntZero+=1
    if cntZero == len(lst):
        raise ValueError('All weights are zero')
    total=0
    for i,w in enumerate(lst):        
        total= total+ w ** (1.0 / T)
    cummulative=0
    rnd =random.random()
    for i, w in enumerate(lst):
        cummulative = cummulative+((w ** (1.0 / T))/total)
        print(rnd,cummulative,total)
        if rnd <= cummulative:
            print(i)
            break
        
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

'''  Write a function solve_expression(expr) that takes an expression (in this special array format) and returns its value.

💡 Hint: Use recursion to handle nested expressions.'''

def solve_expression(exp):
    try:
        # If exp is a number, just return it
        if isinstance(exp, int) or isinstance(exp, float):
            return exp
        if len(exp) != 3:
            raise ValueError("Expression must be [operator, operand1, operand2]")

        operator, left, right = exp

        if not isinstance(operator, str):
            raise ValueError("First element must be an operator")    

        # Solve left and right first (recursion)        
        left_value = solve_expression(left)
        right_value = solve_expression(right)
        # Do the operation
        if operator == '+':
            return left_value + right_value
        elif operator == '-':
            return left_value - right_value
        elif operator == '*':
            return left_value * right_value
        elif operator == '/':
            if right_value == 0:
                raise ZeroDivisionError("Division by zero")
            return left_value / right_value
    except(ValueError,ZeroDivisionError) as e:
        print('Error:'+str(e))


'''Write a function to print all the permutations of a string containing uinque letters
example input: pr output: pr rp input pri output: pri pir rpi rip ipr irp '''

def str_per(str, target_str= None,prev_index=None,ctr=None):  
  len_str= len(str)
  if ctr==None:
    ctr = math.factorial(len_str)
  source_str=[]  
  if prev_index == None:
    prev_index = 0
  if target_str==None:
    target_str=[] 
  if prev_index < len_str:        
    for c in str:
      source_str.append(c) #['A','B','C']
    for k, m in enumerate(source_str):
      val = str[k];  #A B
      for n in source_str:
        if n != str[k]:
          val = val+n
      if not val in target_str:
        target_str.append(val) #[ABC , BAC, CAB]
        #print(m,target_str)
        
    if prev_index+ 1<len_str:
        source_str[prev_index], source_str[prev_index+1]= source_str[prev_index+1],source_str[prev_index]
        new_str = "".join(source_str)
        #print(new_str,prev_index+1)
        str_per(new_str,target_str,prev_index+1, ctr-1)
    else:
      if ctr >0:
        prev_index=0
        str_per(str,target_str,prev_index, ctr-1)
  return target_str

#**********************************************************************************************#
   ## Start: Dictionary exercises
#**********************************************************************************************#
'''Write a function word_count(text) that:
    Takes a string text as input.
    Splits the text into words (you can use split()).
    Counts how many times each word appears using a dictionary.
    Returns the dictionary of word counts.'''
   
def word_count(text):
    result = {}
    text_lst = text.split(" ")
    for key in text_lst:
        if  key in result.keys(): 
                result[key] = int(result[key])+1
        else:
            result[key] ="1"
    return result
            
'''Write a function find_anagrams(text) that:

    Splits the given text into words.

    Uses a dictionary to group words that are anagrams of each other.

    Returns a dictionary where:

    The key is the sorted letters (like "eilnst").
    The value is a list of words that are anagrams.'''

def find_anagrams(text):
    result = {}
    text_lst = text.split(" ")
    for key in text_lst: 
         sorted_key = "".join(sorted(key))
         if  sorted_key in result.keys(): 
              result[sorted_key] =  result[sorted_key]+", "+key 
         else:
            result[sorted_key] =  key
    return result            

'''We can build a simple expense tracker using a dictionary:

The keys will be the expense heads (like "food", "rent", "travel").
The values will be the total amount spent under that head.
We will write two functions:

update_expenses(expense_list, expenses_dict) → updates the dictionary with new expenses.

expense_list is a list of tuples like [("food", 200), ("rent", 1000)].
expenses_dict is the dictionary where totals are stored.
print_expenses(expenses_dict) → prints the overall expenses under each head in a clean way.'''   

def update_expenses(expense_list, expenses_dict):
    if expenses_dict == None:
        expenses_dict ={}
    for ele in expense_list:
        key = ele[0]
        val = ele[1]
        if not key in expenses_dict:
            expenses_dict[key]=val             
        else:
            new_val =int(expenses_dict[key])+int(val) #int(result[key])+1
            expenses_dict[key] =new_val
        #print(expenses_dict)
             
def print_expenses( expenses_dict):
    for dict_val in expenses_dict:
        key = dict_val
        val = expenses_dict[dict_val]
        print(dict_val,":",expenses_dict[dict_val])
       
   
   
   #**********************************************************************************************#
   ## End: Dictionary exercises
   #**********************************************************************************************#