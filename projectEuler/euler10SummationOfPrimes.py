'''
Project Euler 10
Faster solution implementing Sieve of Eratosthenes
'''

import time
t = time.time()

sieve = [True]*2000000
sieve[0] = False
primes = []

for i in range( 2, 2*10**6 ):

    if sieve[i-1]:

        primes.append(i)

        for j in range( i*i, 2*10**6, i ):

            sieve[j-1] = False

            
print sum(primes)
print 'Time elapsed:', time.time() - t
