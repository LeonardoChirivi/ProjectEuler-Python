'''The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''
from math import sqrt
import time
t= time.time()

def isPrime (n):
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            return False
    return True

numbers= [i for i in xrange(2,2000000) if isPrime(i)==True]
print sum(numbers)
Dt= time.time() - t
print 'took: ',Dt

'''
marked = [0] * 1000000
value = 3
s = 2
while value < 1000000:
    if marked[value] == 0:
        s += value
        i = value
        while i < 1000000:
            marked[i] = 1
            i += value
    value += 2
print s
'''
