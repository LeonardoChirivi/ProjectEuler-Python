# -*- coding: utf-8 -*-
'''
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers
is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''


def isPalindrome (n):
    revN= str(n)[::-1]
    return n==int(revN)


product=0
Max=0
for i in range(100,1000):
    for j in range(100,1000):
        product= i*j
        if isPalindrome(product):
            if product > Max:
                Max= product

                
print Max
         
            
