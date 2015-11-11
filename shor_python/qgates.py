# Quantum gates.
# Assumes input qubits are arrays of two complex numbers.

from math import sqrt
import numpy as np
# NOT gate
def qnot(q):
    return np.array([q[1],q[0]], dtype = complex)

# Hadamard
def hadamard(q):
    return np.array([sqrt(0.5)*(q[0]+q[1]),sqrt(0.5)*(q[0]-q[1])], dtype = complex)

# Rotate
# takes in theta as angle of rotation in radians
def rotate(q,theta):
    return np.array([cos(theta)*q[0]-sin(theta)*q[1],sin(theta)*q[0]+cos(theta)*q[1]], dtype = complex)

# Phase flip (Z)
# acts as NOT gate in the plus/minus basis
def phase_flip(q):
    return np.array([q[0],-q[1]], dtype = complex)

# CNOT
# takes in two-qubit system vector
# performs NOT gate on target vector if first qubit is in state 1
def CNOT(q):
    return np.array([q[0],q[1],q[3],q[2]], dtype = complex)
        
