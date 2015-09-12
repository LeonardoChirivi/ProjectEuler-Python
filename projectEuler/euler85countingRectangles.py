'''
euler85 counting rectangles
'''

maxRectangles = 2000000
maxArea = 0
rect = 0

for m in range(1, 2000):
    for n in range( m, 2000 ):
        rectangles = m * n * (m+1) * (n+1) /4
        if abs(rect-maxRectangles)  > abs(rectangles-maxRectangles):
            maxArea = m*n
            rect = rectangles
        if rectangles > maxRectangles:
            break

print maxArea
