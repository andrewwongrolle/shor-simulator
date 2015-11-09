# Matrix implementation of the quantum fourier transform.
# Takes in a normalized ket implemented as an np array.

import numpy as np
import math
import cmath

def qft(in_qubits):
    # dimension of the QFT
    M = len(in_qubits)
    # the Mth root of unity
    p = complex(0, 2*math.pi / M)
    omega = cmath.exp(p)
    # the ijth entry of the QFT matrix is omega^((i-1)(j-1))
    transform = np.ones((M,M), dtype=complex)    
    for x in xrange(M):
        for y in xrange(M):
            transform[x][y] = (1 / math.sqrt(M)) * pow(omega,x*y)
    return np.dot(transform,in_qubits)
    

