'''
euler 24
lexicographic permutation
'''
from itertools import permutations
perm = list( permutations( range(10) ) )
print perm[1000000-1]
