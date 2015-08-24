'''
Find first 10 digits of sum of 100 50-digits numbers.
'''

f= open('largeSum.txt','r')

righe= f.readlines()
Sum= 0

for i in range(len(righe)-1):
    Sum+= int(righe[i])

    
print str(Sum)[0:10]
