# Takes in a normalized vector representing system of qubits.
# "Measures" the system and returns the resulting state.

import random
import cmath
import numpy as np

def measure(qubits):
    # Gets random float in the range [0,1)
    random.seed()
    n = random.random()
    print n
    # multiply by complex conjugate element-wise to obtain amplitude squared
    amp_sq = []

    for q in qubits:
        print q
        amp_sq.append(q * q.conjugate()) 
        
    # The cumulative sum of this list represents a histogram.
    # Say the system is in state j with probability p:
    # Thus amp_sq(j) = p. 
    # Therefore, we have cumsum(amp_sq)[j+1] - cumsum(amp_sq)[j] = p.
    # The probability that a uniformly random float n in [0,1] is
    # in any given range [a,b] where b-a = p is p.
    # Therefore we find the first element in the cumsum array > n.
    
    hist = np.cumsum(amp_sq)
    for i in range(len(hist)):
        if hist[i] > n:
            return i
    return -1
    
