#! usr/bin/python
# This porgram tells whether the given graph has a clique of size k or not

import deg_check as dc

from numpy import *
import xlrd as xlrd

r = raw_input('Pls enter the name of sheet in which adjcent matrix is being stored \n ')
wb = xlrd.open_workbook(r)#To get workbook
sh = wb.sheet_by_index(0)#To get first sheet

Adj_mat = []#Initialisation
V = []

for rn in range(sh.nrows):# creating Adj_mat and V
      Adj_mat = Adj_mat + [sh.row_values(rn)]
      V.append(rn+1)

k = input('Enter the size of clique we are looking for  ')
k=k-1
flag =0
D = [0 for i in range(0,len(Adj_mat))]

while flag==0:
      for i in range(0,len(Adj_mat)):
            D[i]=sum(Adj_mat[i])

      Adj_mat,D = dc.min_deg_check(Adj_mat,D,k)

      if len(Adj_mat)==0:
            print '1.No clique exists'
            break

      d_max_i = D.index(max(D))
      if max(D) < k:
            print '2.No clique exist'
            break

      temp = Adj_mat[d_max_i]
      temp1 = [0 for i in range(0,len(Adj_mat))]
      temp2 = [0 for i in range(0,len(Adj_mat))]
      q=1# to measure the size of clique
      Covered = [d_max_i]
      print Covered
      while sum(temp)!= 0:
            k1=0
            for i in range(0,len(Adj_mat)):
                  if i in Covered != True:
                        print i
                        print sum(temp1)
                        for i1 in range(0,len(Adj_mat)):
                              temp1[i1] = temp[i1]*Adj_mat[i][i1]
                        print 'sum(temp1) is ',sum(temp1)
                        print 'k1 is ',k1
                        a = input('Script check ')
                        if k1 < sum(temp1):
                              k1 = sum(temp1)
                              temp2 =temp1
                              i_sto = i
            temp = temp2
            Covered = Covered + [i_sto]
            q=q+1
            
      if q < k:
            for j in range(0,len(Adj_mat)):
                  del Adj_mat[j][d_max_i]
            del Adj_mat[d_max_i]
            del D[d_max_i]
      else:
            print 'Clique of given size exist'
            break
      
            


      
            
      




      

                




