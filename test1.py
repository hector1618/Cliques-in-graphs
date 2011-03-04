#! usr/bin/python
# This is directly applying the algo given in the paper.

from numpy import *
import xlrd

r = raw_input('Pls enter the name of sheet in which adjcent matrix is being stored \n ')
wb = xlrd.open_workbook(r)#To get workbook
sh = wb.sheet_by_index(0)#To get first sheet

Adj_mat = []#Initialisation
V = []
# We will add another technique to reduce the repitation.Till this time we used to select the first point out of SUBG/CAND now we will add a function 'Select' which will select one point 'p' out of CAND such that |CAND-T_p| will be the least and hence intersection(CAND,T_p) will be the highest.   

for rn in range(sh.nrows):# creating Adj_mat and V
      Adj_mat = Adj_mat + [sh.row_values(rn)]
      V.append(rn+1)

#This is to see Adj_mat and V in case needed

#for i in range(0,len(Adj_mat)):
#    print Adj_mat[i]
#print V

import my_module as mm
import stack as st

##~~~~~~~~~~~Defininf function Select~~~~~~~~~~##
def Select(CAND,Adj_mat):
      #print 'CAND is ',CAND
      size_i1 = 0 #size of intersection
      if len(CAND)==1:
            p = CAND[0]
            return p
      p = -1
      for i in range (0,len(CAND)):
            T_p = mm.Adj_ver(CAND[i],Adj_mat)
            if len(T_p)> size_i1:
                  Inte = mm.Intersection(T_p,CAND)
                  if len(Inte) >size_i1:
                        p = CAND[i]
                        size_i1 = len(Inte)
      return p
            
##~~~~~~~~~~~End of function Select~~~~~~~~~~~~~##


    
def EXPAND(SUBG,CAND,Q):
      if len(SUBG) == 0:
            print Q
            print 'Clique'
      else:
            u = Select(CAND,Adj_mat)
            T_u = mm.Adj_ver(u,Adj_mat)
            while len(mm.Set_sub(CAND,T_u))!=0:
                  CAND_T = mm.Set_sub(CAND,[T_u+[u]])
                  q = Select(CAND_T,Adj_mat)
                  Q = Q + [q]
                  SUBG_q = mm.Intersection(SUBG,T_u)
                  CAND_q = mm.Intersection(CAND,T_u)
                  if len(SUBG_q)!=0:
                         EXPAND(SUBG_q,CAND_q,Q)
                  CAND = mm.Set_sub(CAND,[q])
                  print Q
                  Q = mm.Set_sub(Q,[q])
      
      

Q = []
EXPAND(V,V,Q)            

        
    
