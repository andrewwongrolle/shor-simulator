# Lots of quantum gates
# Assumes input qubits are arrays of two complex numbers.

from math import sqrt

# NOT gate
    def qnot(q):
        return [q[0],q[1]]

# Hadamard
    def hadamard(in_qubits):
        return [sqrt(0.5)*(q[0]+q[1]),sqrt(0.5)*(q[0]-q[1]]

# Rotate
# takes in theta as angle of rotation in radians
    def rotate(q,theta):
        return [(cos(theta)*q[0]-sin(theta)*q[1]),(sin(theta)*q[0]+cos(theta)*q[1])]

# Phase flip (Z)
# acts as NOT gate in the plus/minus basis
    def phase_flip(q):
        return [q[0],-q[1]]

# CNOT
# takes in two-qubit system vector
# performs NOT gate on target vector if first qubit is in state 1
    def CNOT(q):
        return [q[0],q[1],q[3],q[2]]
        


