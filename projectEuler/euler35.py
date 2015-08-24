'''
The number, 197, is called a circular prime because all rotations
of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100:
2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
'''
from math import sqrt

def isPrime (n):
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            return False
    return True 

primes=[i for i in xrange(1000000) if isPrime(i)]
