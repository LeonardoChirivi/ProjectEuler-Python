'''
12- Highly divisible triangular number

~~~ https://it.wikipedia.org/wiki/Divisore#Numero_di_divisori ~~~
~~~      produttoria numero divisori                          ~~~


         d(n) = (\nu_1 + 1) (\nu_2 + 1) ... (\nu_M + 1) 
'''

import time
t= time.time()

def primeFactorization (n):
    ''' returns a list with exponents of all prime factors '''
    exp = [] #lista con esponenti dei fattori primi den numero
    c = 2
    ex = 0 # esponenti dei fattori
    # fattorizzazione
    while n > 1:
        while n%c == 0:           
            n /= c
            ex += 1
        c += 1
        
        if ex > 0:
            exp.append(ex)
        ex = 0
    return exp


def combinatorics (n):
    ''' return number of divisor of a given number using combinatorics formula '''
    
    exponents = primeFactorization(n)
    nDiv = 1
    
    for exp in exponents:
        nDiv *= (exp+1)
    return nDiv

n = 1
Tn = ( n * ( n+1 ) ) / 2
        
while combinatorics(Tn) < 500:
    n += 1
    Tn = ( n * ( n+1 ) ) / 2
print Tn
   
print 'took',str(time.time() - t)
