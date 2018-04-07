# Quantum utility functions
import numpy as np
import scipy as sp
import scipy.linalg

# Kronecker product of n matrices
def nkron(*args, **kwargs):
    prod = np.eye(1)
    eyes = kwargs.pop('eyes', [])
    for idx, arg in enumerate(args):
        if (idx in eyes) and (arg.shape[0] == arg.shape[1]):
            prod = _fast_eye_kron(prod, arg.shape[0])
        else:
            prod = np.kron(prod, arg)
    return prod 

# Kronecker product of a matrix A with itself n times
def self_kron(A, n):
    prod = np.eye(1)
    for _ in range(n):
        prod = np.kron(prod, A)
    return prod

# Kronecker product of the identity matrix with itself n times
def i_kron(n):
    return np.eye(2**n, dtype='complex')

# Normalizes the state s
def normalize(s):
    return (s/sp.linalg.norm(s))

# Fast version of np.kron(matrix, np.eye(N))
def _fast_eye_kron(A, N):
    m, n = A.shape
    out = np.zeros((m, N, n, N), dtype=A.dtype)
    r = np.arange(N)
    out[:,r,:,r] = A
    out.shape = (m*N, n*N)
    return out
