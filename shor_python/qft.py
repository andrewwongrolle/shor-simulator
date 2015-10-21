# Matrix implementation of quantum fourier transform.
# Takes in a normalized ket implemented as an np array.

import numpy as np
import math
import cmath
def qft():
    # dimension of the QFT
    # M = len(in_qubits)
    M = 512
    p = complex(0, 2*math.pi / M)
    omega = cmath.exp(p)
    print omega
    return
    
qft()    
