#generate all strings of length n and sum m

import numpy as np

'''
This function generates a list containing all ordered strings of
length n that add up to m such that each component is positive

Inputs: n, the lenght of the string
        m, the sum of the string
        n <= m

Outputs: a list containing the strings

'''

def posstringset(n,m):
    if n == m:
        return [np.ones(n,dtype=int)]
    else:
        prev_set = posstringset(n,m-1)
        new_set = []
        for i in range(n):
            for x in prev_set:
                y = np.sort(x + np.eye(n)[i])
                if containedinset(y,new_set) == False:
                    new_set.append(y)
    return new_set
                
                
'''
This function takes in a numpy array and compares it to a list
of numpy arrays. If it is in the array, it outputs True, else,
it outputs False

Inputs: tup, a numpy array, for example. array([2,1,1,1])
        bag, a list of numpy arrays that resemble tup
        
Outputs: True if bag contains tup
         False, else
'''

def containedinset(tup,bag):
    for x in bag:
        if (tup == x).all() == True:
            return True
            break
    return False
        
'''
This function does the same as posstringset but it also
gets the entries where we have 0s
'''

def stringset(n,m):
    if m == 0:
        return [np.zeros(n,dtype=int)]
    else:
        prev_set = stringset(n,m-1)
        new_set = []
        for i in range(n):
            for x in prev_set:
                y = np.sort(x + np.eye(n)[i])
                if containedinset(y,new_set) == False:
                    new_set.append(y)
    return new_set