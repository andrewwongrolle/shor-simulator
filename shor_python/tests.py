import numpy as np
from qutils import *
import pretty_print_complex as ppc
import sample_qubits
from qgates import *
from qft import fqft, mqft

def strict_test_equal(A, B):
    assert(np.allclose(A, B))

# tests for quantum gates implementation 
strict_test_equal(CNOT, CREMOTE(NOT, 0, 1, 2))
strict_test_equal(nkron(CNOT, I, eyes=[1]), CREMOTE(NOT, 0, 1, 3))
strict_test_equal(CNOT, CREMOTE(NOT, 0, 1, 2))
CNOT03 = nkron(P0, I, I, I, I) + nkron(P1, I, I, NOT, I, eyes=[1, 2, 4]) 
strict_test_equal(CNOT03, CREMOTE(NOT, 0, 3, 5))

# tests for quantum Fourier transform
f = 0.5 * np.array([[1],[1],[1],[1]], dtype = complex) 
g = nkron(sample_qubits.zero, sample_qubits.zero)
h = nkron(sample_qubits.zero, sample_qubits.one)
test_states = [f,g,h]

for state in test_states:
    strict_test_equal(mqft(state), fqft(state))

def qft_test(f, x):
    print "Taking QFT of ", 
    ppc.print_state(x)
    print "\n..."
    ppc.print_state(f(x))
    print "\n"
