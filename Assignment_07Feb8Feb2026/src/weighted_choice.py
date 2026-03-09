    
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