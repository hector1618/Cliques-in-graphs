#! usr/bin/python

# This script file is used to create a module which will contain all the required function
# Adj_mat i.e. Adjecency matrix is supposed to be defined in the main program and here that is taken as input argument.
# The functions are :
#  1) T = Adj_ver(p) returns adjecent vertices of point p
#  2) C = Interseaction(A,B) returns the intersection of two sets A and B
#  3) C = Set_sub(A,B) subtract set B from set A
#  4) A = Coloring(R,Adj_mat) To color the given subset R of a graph represented by Adj_mat

def Adj_ver(p,Adj_mat):
    T = [-1] # this is used to remove inconsistency in runtime
    Am = Adj_mat[p-1]
    for i in range (0,len(Adj_mat)):
        if (Am[i]==1):
            T = T + [i+1]
    del T[0]
    return T
##~~~~~~~~~~~~~ End of function Adj_ver ~~~~~~~~~~~~~~~##
def Intersection(A,B):
    C = []
    for i in range (0,len(A)):
        for j in range (0,len(B)):
            if(A[i]==B[j]):
                i1 = A[i]
                C = C + [i1]
    return C
##~~~~~~~~~~~~~ End of function Intersection ~~~~~~~~~~~~##

def Set_sub(A,B):
    C = A[:]
    i = 0;
    for j in range(0,len(B)):
        i = 0
        while i<len(C):
            if B[j]==C[i]:
                del C[i]
                if len(C)==0:
                    return C
                i = i-1
            #end of it
            i=i+1
    return C
                   
         
        
##~~~~~~~~~~~~~~End of function Intersection~~~~~~~~~~~~~##


def Coloring(R,Adj_mat):
    # R is a subset of graph represented by Adj_mat 
    class Vertex(p):
        def ver(self,p):
            return p
        def deg(self,p,Adj_mat):
            T_p = Adj_ver(p,Adj_mat)
            return len(T_p)
        def adj_v(self,p,Adj_mat):
            T_p = Adj_ver(p,Adj_mat)
            return T_p

            
