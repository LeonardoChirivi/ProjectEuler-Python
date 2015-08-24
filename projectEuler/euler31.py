'''
coin sums
euler 31
'''
combo = 0
'''
for i in range( 201 ):
    for j in range( i, 101 ):
        for k in range( j, 51 ):
            for x in range( k, 21 ):
                for y in range(  x, 11):
                    for a in range( y, 6 ):
                        for b in range( a, 200 ):
                            
                           # print i,j,k,x,y,a,b
                            if i+j+k+x+y+a+b == 200:
                                combo += 1


print combo
'''
solution = 0
for p1 in range(0,201):
        for p2 in range(0,201-p1,2):
            for p5 in range(0,201-(p1 + p2),5):
                for p10 in range(0,201-(p1 + p2 + p5),10):
                    for p20 in range(0,201-(p1 + p2 + p5 + p10),20):
                        for p50 in range(0,201-(p1 + p2 + p5 + p10 + p20),50):
                            for p100 in range(0,201-(p1 + p2 + p5 + p10 + p20 + p50),100):
                                for p200 in range(0,201-(p1 + p2 + p5 + p10 + p20 + p50 + p100), 200):
                                    print p1,p2,p5,p10,p20,p50,p100,p200
                                    if p1 + p2 + p5 + p10 + p20 + p50 + p100 + p200 == 200:
                                        solution += 1


print solution
