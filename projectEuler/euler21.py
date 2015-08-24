'''
amicable numbers euler 21
'''
import time
t = time.time()

def divisorsSum (n):
    return  sum( [i for i in range(1,(n/2)+1) if n%i==0] )    

l = []

for i in range( 1, 10000 ):
    if i in l:
        continue
    n1 = divisorsSum(i)
    for j in range( i+1, 10000 ):
        if n1 == j and divisorsSum(j) == i:
            #print n1, divisorsSum(j), i, j
            l.append(i)
            l.append(j)
            break

print sum(l)
print 'took',str( time.time() - t )

'''

took 6.71509504318  ~~~ [i for i in range(1,n) if n%i==0] 

took 4.70858883858  ~~~ [i for i in range(1,(n/2)+1) if n%i==0] 



'''
