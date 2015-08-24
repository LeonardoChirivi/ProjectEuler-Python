from math import sqrt
import time
t = time.time()

def isPrime(n):
    for i in range(2, int(sqrt(n)+1)):
        if n%i == 0:
            return False
    return True

Ma = 0
Mb = 0
Mn = 0

for a in range(-1000, 1001):
    for b in range(-1000, 1001):
        n=0
        while isPrime(abs(n**2+a*n+b)):
            n += 1
        if n > Mn:
            Ma = a
            Mb = b
            Mn = n

print Ma, Mb, Mn, '---->',Ma*Mb
print 'took',time.time()-t 
