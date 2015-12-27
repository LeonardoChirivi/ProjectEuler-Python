'''
Project Euler 10
Faster solution implementing Sieve of Eratosthenes
'''

import time
t = time.time()

sieve = [True]*2000000
sieve[0] = False
primes = 0

for i in xrange( 2, 2*10**6 ):

    if sieve[i-1]:

        primes += i

        for j in xrange( i*i, 2*10**6, i ):

            sieve[j-1] = False

            
print primes
print 'Time elapsed:', time.time() - t
