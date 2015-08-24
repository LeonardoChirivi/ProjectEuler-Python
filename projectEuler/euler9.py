'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''
import time

t= time.time()

def isPitagorean ( a, b, c ):
    return a**2 + b**2 == c**2

c= True

while c:
    for i in xrange(1, 500):
        for j in xrange(i+1,500):
            k= 1000 - ( i+j )
            if i+j+k == 1000 and isPitagorean( i,j,k ):
                print i ,j, k,'\t', i*j*k
                c= False
                    
                
Dt= time.time() - t

print 'took %f seconds' %(Dt)
        

