# -*- coding: utf-8 -*-
'''
Largest product in a grid Project Euler problem n.11
'''
import time
t= time.time()

maximum= 0

f= open( 'productGrid.txt', 'r' )
lines= []

for line in f:
    
    # nell' array lines ci sono tutte le righe del file, ogni riga è un array
    lines.append( line.split(' ') )
    
f.close()


# search the orizzontal rows
for item in lines:
    for i in range( len(item)-1 ):
        product= 1
        if i == 16:
            break
        for j in range(4):
            product *= int( item[i+j] )
            if product > maximum:
                maximum = product


# check vertical lines
index= 0
c= True

while c:
    column= []

    
    for n in lines:
        column.append(n[index])
    index +=1
    
    for i in range( len(column)-1 ):
        product= 1
        if i == 16:
            break
        for j in range(4):
            product *= int( column[i+j] )
            if product > maximum:
                maximum = product

    if index > 19:
        c= False
    

# diagonal using 2d array
prod= 0

for i in range(16):
    for j in range(16):
        prod= int(lines[i][j]) * int(lines[i+1][j+1]) * int(lines[i+2][i+2]) * int(lines[i+3][j+3])
        if prod > maximum:
            maximum = prod


for i in range(3, 20):
    for j in range(16):
        prod= int(lines[i][j]) * int(lines[i-1][j+1]) * int(lines[i-2][j+2]) * int(lines[i-3][j+3])
        if prod > maximum:
            maximum = prod

Dt= time.time() - t
print maximum
print Dt























        
