# sample qubits for testing

import numpy as np
from math import sqrt

# four dimensional basis vectors for two qubits system
e1 = np.array([1,0,0,0], dtype = complex) # |00>
e2 = np.array([0,1,0,0], dtype = complex) # |01>
e3 = np.array([0,0,1,0], dtype = complex) # |10>
e4 = np.array([0,0,0,1], dtype = complex) # |11>

# plus/minus basis vectors for one qubits systems
plus = (1 / sqrt(2)) * np.array([1, 1], dtype = complex)
minus = (1 / sqrt(2)) * np.array([1,-1], dtype = complex)

# Bell states
#  1 / sqrt(2) * |01> + |10>
psi_plus = 1 / sqrt(2) * np.array([0,1,0,1], dtype = complex) 

# 1 / sqrt(2) * |01> - |10>
psi_minus = 1 / sqrt(2 ) * np.array([0,1,0,-1], dtype = complex)   

# 1 / sqrt(2) * |00> + |11>
phi_plus = 1 / sqrt(2 ) * np.array([1,0,0,1], dtype = complex)   

# 1 / sqrt(2) * |00> - |11>
phi_minus = 1 / sqrt(2 ) * np.array([1,0,0,-1], dtype = complex)   

