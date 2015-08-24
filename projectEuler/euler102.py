# -*- coding: utf-8 -*-
'''
Three distinct points are plotted at random
on a Cartesian plane, for which -1000 ≤ x, y ≤ 1000, such that
a triangle is formed.

Consider the following two triangles:

A(-340,495), B(-153,-910), C(835,-947)

X(-175,41), Y(-421,-714), Z(574,-645)

It can be verified that triangle ABC contains the origin,
whereas triangle XYZ does not.

Using triangles.txt (right click and 'Save Link/Target As...'),
a 27K text file containing the co-ordinates of one thousand "random"
triangles, find the number of triangles for which the interior contains
the origin.
'''
# appartenenza punto P: area ABC= ABP +  BCP + CAP
    

def area (xa, ya, xb, yb, xc, yc):

    a= 0.5 * abs( (xa-xc) * (yb-ya) - (xa-xb) * (yc-ya) )

    return a


nTriangoli= 0

f= open('triangles.txt', 'r')

for lines in f:
    
    # coordinate triangolo
    tr= lines.split(',')

    # calcolo area tringolo principale
    areaTr= area( int(tr[0]), int(tr[1]), int(tr[2]), int(tr[3]), int(tr[4]), int(tr[5]) )
    
    # calcolo aree ABP(area1), BCP(area2), CAP(area3), e la loro somma
    area1= area( int(tr[0]), int(tr[1]), int(tr[2]), int(tr[3]), 0, 0 )
    area2= area( int(tr[2]), int(tr[3]), int(tr[4]), int(tr[5]), 0, 0 )
    area3= area( int(tr[0]), int(tr[1]), int(tr[4]), int(tr[5]), 0, 0 )

    subaree= area1 + area2 + area3

    if areaTr == subaree:
        nTriangoli+=1
    
f.close()

print nTriangoli
