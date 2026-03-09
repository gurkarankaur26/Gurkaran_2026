
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