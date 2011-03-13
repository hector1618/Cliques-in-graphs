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


import my_module as mm
import stack as st

##~~~~~~~~~~~Defininf function Select~~~~~~~~~~##
def Select(CAND,Adj_mat):
      size_i1 = -1 #size of intersection
      if len(CAND)==1:
            p = CAND[0]
            return p
      p = -1
      for i in range (0,len(CAND)):
            T_p = mm.Adj_ver(CAND[i],Adj_mat)
            if len(T_p)> size_i1:
                  Inte = mm.Intersection(T_p,CAND)
                  if len(Inte)>size_i1:
                        p = CAND[i]
                        size_i1 = len(Inte)
      return p
            
##~~~~~~~~~~~End of function Select~~~~~~~~~~~~~##

      
      


##~~~~~~~~~~~Defining function Expand~~~~~~~~~~##
def Expand(p,Q,CAND,s):
      Q = Q + [p]
    #p is a point,Q is a clique formed so for,CAND is canditate set(replacing SUBG) at that time and s is stack used
      while len(CAND)!=0:
            p1 = Select(CAND,Adj_mat)
            T_p1 = mm.Adj_ver(p1,Adj_mat)
            CAND_t = CAND[:]
            CAND_t = mm.Set_sub(CAND_t,[p1])
            CAND_t = mm.Set_sub(CAND_t,T_p1)
            while len(CAND_t)!= 0:
                  p2 = Select(CAND_t,Adj_mat)
                  T_p2 = mm.Adj_ver(p2,Adj_mat)
                  CAND_n = mm.Intersection(CAND,T_p2)
                  s.push(p2,Q,CAND_n)
                  CAND_t = mm.Set_sub(CAND_t,[p2])
                  CAND_t = mm.Set_sub(CAND_t,T_p2)
                
            CAND = mm.Intersection(CAND,T_p1)
            Q = Q + [p1]
      return Q
##~~~~~~~~~~~~End of function Exapand~~~~~~~~~~~##



##~~~~~~~~~~~~Main program stats~~~~~~~~~~~~~~~~##

Cliques = []#The final ans will be stored in this    
s = st.Cla_stack()#Defining the stack
V_temp = V[:]

while len(V_temp)!=0:
      p = Select(V_temp,Adj_mat)
      Q = []
      T_p = mm.Adj_ver(p,Adj_mat)
      s.push(p,Q,T_p)
      V_temp = mm.Set_sub(V_temp,[p])
      V_temp = mm.Set_sub(V_temp,T_p)


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



    
            

        
    
