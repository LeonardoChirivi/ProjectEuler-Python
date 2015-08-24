'''
euler 19
counting soundays
'''

import calendar

soundays = 0

for year in range( 1901,2001 ):
    for month in range( 1,13 ):
        if calendar.weekday( year, month, 1 ) == 6:
            soundays += 1

print soundays
