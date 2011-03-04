#! usr/bin/python
# This porgram eliminates all the vertices of the graph and return the Adj_mat after reduction

from numpy import *


def min_deg_check(Adj_mat,D,k):
      while min(D)<k:
            i1=len(D)-1
            while i1>=0:
                  if D[i1]<k:
                        for j in range(0,len(Adj_mat)):
                              del Adj_mat[j][i1]
                        del Adj_mat[i1]
                        del D[i1]
                  i1=i1-1    

            for i in range(0,len(Adj_mat)):
                  D[i]=sum(Adj_mat[i])
            #print D
            if len(D)==0:
                  break
            
            
      return Adj_mat,D


            
                




