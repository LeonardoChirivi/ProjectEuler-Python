'''
Euler 76
Counting summations
'''
n = 100
numbers = range(1, n)
ways = [1] + [0]*n

for number in numbers:
    
    for i in range(number, n+1):
        
        ways[i] += ways[i-number]


print ways[n]
