'''
Maximum path sum I, II
'''
maxsum= 0

f= open('maxPathSum2.txt', 'r')
triangle= []

for lines in f:
    triangle.append(lines.split(' '))
f.close()

triangle.reverse()

for x in range( len(triangle) ):
    for y in range( len(triangle[x]) ):
        triangle[x][y] = int(triangle[x][y])
        

for x in range( len(triangle) ):
    
    y=0
    k, j = 0, 1

    while j < len( triangle[x] ):

            triangle[x+1][y] +=  max( triangle[x][k], triangle[x][j] )

            k+=1; j+=1; y+=1
    x+=1
    
    
print triangle[ len(triangle)-1 ][0]
