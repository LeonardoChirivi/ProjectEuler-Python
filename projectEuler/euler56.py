'''
A googol (10100) is a massive number: one followed by one-hundred zeros;
100100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, ab, where a, b < 100, what
is the maximum digital sum?

'''
import time
t= time.time()

def digitSum (n):
    dgSum = 0

    while n > 0:
        
        dgSum += n%10
        n /= 10

    return dgSum

    
a, b = 99, 99

maxSum = 0

while a > 0:
    
    while b > 0:
        
        tmp = digitSum( a**b )
        
        if tmp > maxSum:
            maxSum = tmp
            
        b -= 1
    a -= 1

d= time.time() - t

print 'Maimum digit sum: ', maxSum
print 'Took: ', d
    