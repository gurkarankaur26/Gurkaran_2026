
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