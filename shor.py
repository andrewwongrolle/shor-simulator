# Simulates Shor's quantum algorithm for factoring.
# Translated from MATLAB.

import random
from fractions import gcd

# Returns random number relatively prime to argument.
def rand_rel_prime(n):
    r = random.randint(2,n-1)
    while gcd(r,n) != 1:
        r = random.randit(2,n-1)
    return r

# the Shor algorithm. Calls the quantum order finding subroutine "find order".

def shor(N):
    # we need to find some number A with even order
    # and A^(order/2) + 1 (mod N) not equal to 0.


