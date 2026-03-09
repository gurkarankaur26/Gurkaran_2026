
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
    
