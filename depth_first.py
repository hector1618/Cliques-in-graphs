#! usr/bin/python
# This program is used in depth first search algorithm.
# The module used are my_module.py and stack.py and numpy and xlrd
# The input data in the form of book1.xls should be present in the current diretory

from numpy import *
import xlrd

r = raw_input('Pls enter the name of sheet in which adjcent matrix is being stored \n ')
wb = xlrd.open_workbook(r)#To get workbook
sh = wb.sheet_by_index(0)#To get first sheet

Adj_mat = []#Initialisation
V = []

for rn in range(sh.nrows):# creating Adj_mat and V
      Adj_mat = Adj_mat + [sh.row_values(rn)]
      V.append(rn+1)

#This is to see Adj_mat and V in case needed

#for i in range(0,len(Adj_mat)):
#    print Adj_mat[i]
#print V

import my_module as mm
import stack as st


##~~~~~~~~~~~Defining funcition Expand~~~~~~~~~~##
def Expand(p,Q,SUBG,s):
    #p is a point,Q is a clique formed so for,SUBG is at that time and s is stack used
    while len(SUBG)!= 0:
        Q = Q + [p]
        T_p = mm.Adj_ver(p,Adj_mat)
        SUBG = mm.Intersection(SUBG,T_p)
        if len(SUBG) > 0:
            p = SUBG[0]
            for i in range (1,len(SUBG)):
                s.push(SUBG[i],Q,SUBG)#Filling up the stack
    return Q
##~~~~~~~~~~~~End of function Exapand~~~~~~~~~~~##


##~~~~~~~~~~~~Main program stats~~~~~~~~~~~~~~~~##

Cliques = []#The final ans will be stored in this    

for i in range (0,len(V)):
    s = st.Cla_stack()#Defining the stack
    Q = [V[i]]
    p = V[i]
    T_p = mm.Adj_ver(p,Adj_mat)
    SUBG = mm.Intersection(V,T_p)
    if len(SUBG)!= 0:
        for i in range (0,len(SUBG)):
            s.push(SUBG[i],Q,SUBG)

        while s.isempty()!= 1:
            p_Q_SUBG = s.pop()
            p = p_Q_SUBG[0]
            p = p[0]#converting list into int
            Q = p_Q_SUBG[1]
            Q = Q[0]#converting item into list
            SUBG = p_Q_SUBG[2]
            SUBG = SUBG[0]
            C = Expand(p,Q,SUBG,s)
            Cliques = Cliques + [C]
##~~~~~~~~~End of main program~~~~~~~~~~~~~##


for i in range (0,len(Cliques)):#Displaying output
    print Cliques[i]


print len(Cliques)
    
            

        
    
