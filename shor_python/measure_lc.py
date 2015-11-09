# Takes in a normalized vector representing system of qubits.
# "Measures" the system and returns the resulting state.

import random
import cmath 
import numpy as np

# Say the system is in state j with probability p:
    # - The probability p that a qubit is in state j is given by
    #   the the jth amplitude multiplied by its complex conjugate.
    # - We can write p as the (sum of the first j+1 elements
    #   of the probability list) - (the sum of the first j elements).
    # - The probability that a uniformly random float n in [0,1] is in 
    #   the interval [a,b] where b-a = p is p.
    # - Therefore we find the first element  <n in the cumulative sum array.

def measure(qubits):
    random.seed()
    n = random.random()
    pr_sum = [qubits[0] * qubits[0].conjugate()]

    for i in range(1, len(qubits)):
        pr_sum.append(qubits[i] * qubits[i].conjugate())
        pr_sum[i] += pr_sum[i-1]
        if pr_sum[i] > n:
            return i

    return -1
