'''
Surprisingly there are only three numbers that can be written as
the sum of fourth powers of their digits:

1634 = 14 + 64 + 34 + 44
8208 = 84 + 24 + 04 + 84
9474 = 94 + 44 + 74 + 44
As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the
sum of fifth powers of their digits.

So lets determine the upper bound. We need to find a number
x*95 which gives us an x digit number. We can do this by hand.
Since 95 = 59049, we need at least 5 digits. 5*95 = 295245, so
with 5 digits we can make a 6 digit number. 6*95 = 354294.
So 355000 seems like a reasonable upper bound to use.
'''

def digitPower (n):
    s = 0
    for num in str(n):
        s += int(num)**5
    return s

numberSum = 0
l = []
for i in range( 2, 355001 ):
    if digitPower(i) == i:
        numberSum += i
        l.append(i)

print numberSum
