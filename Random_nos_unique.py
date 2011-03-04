#! usr/bin/python
# This is used to generate the random number without any repetation. It takes two values (n,N). Returns n random values between [0,N-1],both included

def Random_nos_unique(n,N):
    #initialising the values of a,b,c
    
    U = [i for i in range(N)]
    from datetime import datetime
    t = datetime.now()
    t = t.timetuple()
    a = t.tm_sec
    u1 = a%N
    b = t.tm_min
    i=0
    R = []
    while(i<n):
        R = R + [U[u1]]
        del U[u1]
        N = N-1
        if len(U)==1:
            R=R+[U[0]]
            return R
        u1 = (u1*a+b)%N
        i = i+1
    return R






    

   
    
