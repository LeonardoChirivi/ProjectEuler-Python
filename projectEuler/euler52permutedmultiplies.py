'''
euler52
permuted multiples
'''
from itertools import permutations

for i in range( 1, 10000000 ):
    
    perm = list(permutations(str(i)))

    if tuple(str(2*i)) in perm and tuple(str(3*i)) in perm and tuple(str(4*i)) in perm  and tuple(str(5*i)) in perm  and tuple(str(6*i)) in perm:
        print i
        break
