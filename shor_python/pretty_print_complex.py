import numpy as np
import math
import qgates
from sample_qubits import *

# pretty print complex numbers
def print_c(z):
    if z.real == 0 and z.imag == 0:
        print "0",
    elif z.imag == 1: 
        print "i",
    elif z.imag == -1:
        print "-i",
    elif z.real == 1:
        print "1",
    elif z.real == -1:
        print "-",
    elif z.imag == 0: 
        print "%.3f" % (z.real), 
    elif z.real == 0:
        print "%.3fi" % (z.imag), 
    else:
        print "(%.3f %+.3fi)" % (z.real, z.imag),
  
# prints "n" formatted in binary with leading zeros
def bin_format(n, zeros=0):
    return ("{0:b}".format(n)).zfill(zeros)

# pretty print states
def print_state(q, binary=True):
    for i in xrange(len(q)):
        print_c(q[i])
        if binary:
            print "|" + bin_format(i, int(math.log(len(q), 2))) +  u'\u27E9', 
        else:
            print "|%d" % (i) +  u'\u27E9', 
        if i < len(q)-1:
            print "+",

# pretty print matrices
def print_mat(m):
    return

