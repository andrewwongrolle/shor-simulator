# Matrix implementation of quantum fourier transform.
# Takes in a normalized ket implemented as an np array.

import numpy as np
import math
import cmath
def qft(in_qubits):
    # dimension of the QFT
    M = len(in_qubits)
    print M 
    p = complex(0, 2*math.pi / M)
    omega = cmath.exp(p)
    print 'omega is %05f %+05fi' % (omega.real, omega.imag)
    transform = np.ones((M,M), dtype=complex)    
    for x in xrange(M):
        for y in xrange(M):
            transform[x][y] = pow(omega,x*y)
            print 'x = %d, y = %d, omega^xy = %05f %+05fi' % (x,y,transform[x][y].real, transform[x][y].imag)
    print(transform)
    transform = transform * (1 / math.sqrt(M))
    return np.dot(transform,in_qubits)
    

