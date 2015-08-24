'''
name scores euler 22
'''
import time
t = time.time()

f = open( 'p022_names.txt', 'r' )

for lines in f:
    names = lines.split(',')
f.close()

names = sorted(names)

score = 0

for i in range( len(names) ):
    letterPosition = 0
    for letter in names[i].upper():
        if letter.isalpha():
            letterPosition += ord(letter) ^ 64           
    score += letterPosition * (i+1)

print score
print 'took',str( time.time() - t )
