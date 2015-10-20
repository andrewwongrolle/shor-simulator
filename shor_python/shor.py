# Simulates Shor's quantum algorithm for factoring.
# Translated from MATLAB.

from fractions import gcd
import cmath
import numpy as np
from measure import measure

# Returns random number coprime to argument.
def rand_coprime(N):
    r = random.randint(2,N-1)
    while gcd(r,N) != 1:
        r = random.randint(2,N-1)
    return r

# the Shor algorithm. Calls the quantum order finding subroutine "find_order".

def shor(N):
    # Factoring N has been reduced to the following problem:
        # Find the order r of the function f(x) = a^x (mod N) for random a.
        # If r is odd OR if a^r/2 = -1 (mod N), choose another a.
        # Otherwise, gcd(a^r/2-1,N) and gcd(a^r/2+1,N) are factors of N.
    
    A = rand_coprime(N) # ensure we don't find a nontrivial factor first thing
    r = find_order(A)
    while ( (r % 2 == 0 ) 
    

