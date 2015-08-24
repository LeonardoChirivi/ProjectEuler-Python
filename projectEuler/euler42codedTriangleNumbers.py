'''
Coded triangle numbers
Problem 42
'''
from math import sqrt

f = open( 'euler42words.txt' ,'r' )

for line in f:
    words = line.split(',')

f.close()

triangleWords = 0

for word in words:
    letterSum = 0

    for letter in word:
        if letter.isalpha():
            letterSum += ord(letter)-64

    root = sqrt( (letterSum *8) +1)

    if root - int(root) == 0:
        triangleWords += 1


print triangleWords
