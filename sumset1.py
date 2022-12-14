import numpy as np
from itertools import permutations

'''
The function stringset returns the total set of ascending order m-tuples that add
up to n and have at least k in each bin. 

Inputs: n, a non-negative integer
    	m, a positive integer, m > 2 and m <= n
        optional), a non-negative integer

Output: a list of np.arrays containing all ordered m-tuples in ascending order
'''
def stringset(n,m,k=0):
    q1 = m*k
    #base case
    if n == q1:
        return [k*np.ones(m,dtype=int)]
    else:
        #recursive step
        prev_set = stringset(n-1,m,k)
        new_set = []
        iden = np.eye(m)
        #outer loop runs through 'basic solutions'
        for i in range(m):
            #inner loop goes through the set that was recursively made
            for x in prev_set:
                #add 'basic solution'
                y = np.sort(x + iden[-i])
                #check if new solution is already in the set to eliminate repeats
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
    return False

'''
This function generates a list containing all points on the simplex

Inputs: n,m,k
Outputs: a list of m-dimensional lists,
         containing all points on the simplex 
         section with all m-dim lists, adding to
         n, ea element containing at least k
'''
def Generate_Simplex(n,m,k=0):
    ans = []
    a = stringset1(n,m,k)
    for x in a:
        b = list(permutations(x, m))
        res = []
        [res.append(y) for y in b if y not in res]
        [ans.append(list(y)) for y in res]
    return ans
