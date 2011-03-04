#! usr/bin/python
# This is used to generate the random number

def Random_nos(n,N):
    #initialising the values of a,b,c
    from datetime import datetime
    t = datetime.now()
    t = t.timetuple()
    a = t.tm_sec
    b = t.tm_min
    c = t.tm_hour
    if N%2==0:#To avoid creating of only even no.s
        if (a*b+c)%2==0:
            c = c+1
        
    i=0
    R = []
    #print a,b,c
    while(i<n):
        d = (a*b+c)%N        
        a = b
        b = c
        c = d
        R = R+[d]
        i = i+1
    return R




    

   
    
