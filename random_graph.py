#! usr/bin/python
# Modules used are
# 1)tempfile
# 2)xlwt
# 3)Random_nos_unique 
# This program is used to generate the graphs. There are two input parameter- (n,e). n is number of vertices and e is number of edges. This will create the simple connected graph if e >= n-1

import Random_nos_unique as rnu

n = input("No of vertices : ")
e = input("No of edges : ")

if e > n*(n-1)/2:
    print 'To many edges.Will return complete graph'
    e=n*(n-1)/2

R = rnu.Random_nos_unique(e,n*(n-1)/2)#Random nos generator
C = [[0 for row in range(n)] for col in range(n)]

E = []# Matrix of possible edges
for i in range(0,n):
    for j in range(0,i):
        E=E+[[i,j]]

for i in range(0,e):
    C[E[R[i]][0]][E[R[i]][1]]=1
    C[E[R[i]][1]][E[R[i]][0]]=1

    
from tempfile import TemporaryFile
from xlwt import Workbook
book = Workbook()
sheet1 = book.add_sheet('Sheet 1')
#Writting the graph will
for i in range(0,n):
    for j in range(0,n):
        sheet1.write(i,j,C[i][j])



r = raw_input('Name of the output followed by .xls i.e graph1.xls \n')
book.save(r)
book.save(TemporaryFile())
