#! usr/bin/python
# This is a module which will we used to handle tree structure.
# This function as two main functions
#  1) push(p,Q) pushes the given elements into stacts
#  2) pop() pops put the last element and return it
# and some other complimentery functions like
#  3) isempty() will return 1 is stack is empty 


class Cla_stack:
    def __init__(self): #This is a constructor
        self.Storage = []
    ##~~~~~~~~~End of constructor~~~~~~~~~~~~~~~~~~~~~~##

    def isempty(self):
        if len(self.Storage)==0:
            return 1
        else:
            return 0

    ##~~~~~~~~~~End of function isempty~~~~~~~~~~~~~~~~~##


    def push(self,p,Q,SUBG):    # Storing a point and Q at that time
        self.Storage = self.Storage + [[[p],[Q],[SUBG]]]

    ##~~~~~~~~~~~End of function push~~~~~~~~~~~~~~~~~~~##


    def pop(self):
        p_Q_SUBG = []
        if self.isempty()==0:
            p_Q_SUBG = self.Storage[len(self.Storage)-1]
        del self.Storage[len(self.Storage)-1]
        return p_Q_SUBG

     ##~~~~~~~~~~~End of function pop~~~~~~~~~~~~~~~~~~~~##

