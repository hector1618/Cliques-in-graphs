#! usr/bin/python
# This program is used as a module to color the given graph
# As this is a special module used in the max_cliques, it will return the max of colors and not the matrix

import my_module as mm
from numpy import *
import my_module as mm

def Coloring(R,Adj_mat):
    # R is a subset of graph represented by Adj_mat 
    class Vertex():
        def __init__(self,p,Adj_mat,c=1):
            self.p = p
            self.Adj_mat = Adj_mat
            self.c = c
            
        def ver(self):
            return self.p
        def adj_v(self):
            T_p = mm.Adj_ver(self.p,self.Adj_mat)
            return T_p
        def deg(self):
            return len(self.adj_v())
        def color(self):
            return self.c
        def set_color(self,c):
            self.c=c
            return c

    V_cl=[]
    for i in range(0,len(Adj_mat)):
        V = Vertex(i+1,Adj_mat)
        V_cl = V_cl + [V]

    V_sorted = sorted(V_cl,key=lambda Vertex:Vertex.deg(),reverse=True)
    V_only = []# To stored sorted vertices only 
    for i in range(0,len(V_sorted)):
        V_only = V_only + [V_sorted[i].ver()]
    #print V_only
    
    for i in range(1,len(V_sorted)):#will start from 1 not 0
        v1 = V_sorted[i]#index of v1
        In = mm.Intersection(v1.adj_v(),V_only[0:i])
        Co_used = []
        for i in range(0,len(In)):
              v2 = V_cl[In[i]-1]
              Co_used = Co_used + [v2.color()]
        
        c1 = 1
        while c1 in Co_used != True:
              c1 = c1+1
        v1.set_color(c1)

    V_colors = []
    c_max = 0 # this is the max color used
    for i in range (0,len(V_sorted)):
          v1 = V_sorted[i]
          if c_max > v1.color():
              c_max = v1.color()
    
    return c_max
