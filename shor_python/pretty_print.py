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
   
# pretty print states.
def pretty_print(q):
    for i in xrange(len(q)):
        print_c(q[i])
        print "|%d" % (i) +  u'\u27E9', 
        if i < len(q)-1:
            print "+",
