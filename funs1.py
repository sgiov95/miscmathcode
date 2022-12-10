import numpy as np

'''
function MakeAllSequences
generates all sequences of length n coming from an alphabet of m characters, default m = 2
input: int n, sequence length, and int m, the number of characters (0,1,2,...,m-1)
output: np int array of dimensions m^n by n 
Example:
input: MakeAllSequences(2)
output: array([[0,0],[0,1],[1,0],[1,1]])
'''
def MakeAllSequences(n,m=2):
    if n == 1:
        return np.arange(m,dtype=int).reshape((m,1))
    else:
        x = MakeAllSequences(n-1,m)
        k = m**(n-1)
        w = np.concatenate((np.zeros(k,dtype=int).reshape((k,1)),x),axis=1)
        for i in range(1,m):
            y = np.concatenate((i*np.ones(k,dtype=int).reshape((k,1)),x),axis=1)
            w = np.concatenate((w,y),axis=0)
        return w
            
            
            
            
            
    