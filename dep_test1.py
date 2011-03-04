#! usr/bin/python
# This program is used in depth first search algorithm.
# The module used are my_module.py and stack.py and numpy and xlrd
# The input data in the form of book1.xls should be present in the current diretory

# This section we are used methode to prone. We will we using CAND as set of possible candidate and SUBG = FINI U CAND. Since FINI is null at the starting, we have CAND = SUBG at the starting and then after instead of pushing SUBG we will push intersection(CAND,T_p) where is the vertex we selected 
# We will add another technique to reduce the repitation.Till this time we used to select the first point out of SUBG/CAND now we will add a function 'Select' which will select one point 'p' out of CAND such that |CAND-T_p| will be the least and hence intersection(CAND,T_p) will be the highest.   

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
      if (len(CAND))==1:
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

      
      


##~~~~~~~~~~~Defining function Expand~~~~~~~~~~##
def Expand(p,Q,CAND,s):
      Q = Q + [p]
    #p is a point,Q is a clique formed so for,CAND is canditate set(replacing SUBG) at that time and s is stack used
      while len(CAND)!= 0:
          p1 = Select(CAND,Adj_mat)
          Q = Q + [p1]
          T_p = mm.Adj_ver(p1,Adj_mat)
          CAND = mm.Intersection(CAND,T_p)
          if len(CAND)>0:
                for i in range (1,len(CAND)):
                      T_p = mm.Adj_ver(CAND[i],Adj_mat)
                      CAND_t = mm.Intersection(CAND,T_p)
                      s.push(CAND[i],Q,CAND_t)#Filling up the stack
            #for the first element which needs to proces    
                p = CAND[0]
                Q = Q + [p]
                T_p = mm.Adj_ver(p,Adj_mat)
                CAND = mm.Intersection(CAND,T_p)          
      return Q
##~~~~~~~~~~~~End of function Exapand~~~~~~~~~~~##


##~~~~~~~~~~~~Main program stats~~~~~~~~~~~~~~~~##

Cliques = []#The final ans will be stored in this    
COVR = []

for i in range (0,len(V)):
      s = st.Cla_stack()#Defining the stack
      Q = [V[i]]
      p = V[i]
      T_p = mm.Adj_ver(p,Adj_mat)
      flag = 0 # proceed with this vertex
      for i1 in range(0,len(COVR)):
            if V[i]==COVR[i1]:
                  flag = 1 #
      
      if flag == 0:
            COVR = COVR + T_p #Expanding the set of COVR vertices
            SUBG = mm.Intersection(V,T_p)
            CAND = mm.Intersection(V,T_p)# and FINI = null initially
            if len(SUBG)!=0:
                  while len(CAND)!=0:
                        T_p = mm.Adj_ver(CAND[0],Adj_mat)
                        #CAND_n is Candidates for next iterations
                        CAND_n = mm.Intersection(SUBG,T_p)
                        s.push(CAND[0],Q,CAND_n)
                        CAND = mm.Set_sub(CAND,[CAND[0]])#Removing the p from candidate set as it is being pushed
                        CAND = mm.Set_sub(CAND,T_p)#Reduing the canditate set

                  while s.isempty()!= 1:
                        p_Q_CAND = s.pop()
                        p = p_Q_CAND[0]
                        p = p[0]#converting list into int
                        Q = p_Q_CAND[1]
                        Q = Q[0]#converting item into list
                        CAND = p_Q_CAND[2]
                        CAND = CAND[0]
                        C = Expand(p,Q,CAND,s)
                        Cliques = Cliques + [C]
##~~~~~~~~~End of main program~~~~~~~~~~~~~##


for i in range (0,len(Cliques)):#Displaying output
    print Cliques[i]

print len(Cliques)



    
            

        
    
