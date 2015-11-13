# Order finding quantum subroutine of the Shor algorithm.

import numpy as np
import math

# finds the order r of the periodic function a^r (mod N)
# M and N are the sizes of the two registers respectively
def find_order(a, N):
    # number of qubits in reg1, s.t. N^2 <= 2^t <= 2N^2
    t = int(math.ceil(2 * math.log(N, 2)))
    reg1 = np.zeros(2**t, dtype = complex)
    
    # number of qubits in reg2
    n = int(math.ceil(math.log(N, 2)))
    reg2 = np.zeros(2**n, dtype = complex)
