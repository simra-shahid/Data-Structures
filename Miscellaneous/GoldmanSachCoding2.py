'''
Given an array, find sum of prime numbers of all the individual array element say primeSum. Now make sets of 0s of length of primeSum with k subsets. 
Example: 
If primeSum = 7 (Computed) and k = 2 (Given) 
Then subsets will be {{}{0000000},{0}{000000},{00}{00000},{000}{000},{0000}{000},{00000}{00},{000000}{0},{0000000}{}} = 8
Output = 8

Similarly if k = 3, Output = 36
'''


import math as mt 
  
MAXN = 100001
  
spf = [0 for i in range(MAXN)] 

def sieve(): 
    spf[1] = 1
    for i in range(2, MAXN): 
       
        spf[i] = i 
  
    for i in range(4, MAXN, 2): 
        spf[i] = 2
  
    for i in range(3, mt.ceil(mt.sqrt(MAXN))): 
          
        if (spf[i] == i): 
             
            for j in range(i * i, MAXN, i):  
                  
                
                if (spf[j] == j): 
                    spf[j] = i 
 

def primeList(x): 
    ret = list() 
    while (x != 1): 
        ret.append(spf[x]) 
        x = x // spf[x] 
  
    return ret

    

from itertools import combinations 

def countP(n, k): 
    r = n+k-1
    p = k-1
    r1 = [ i for i in range(0,r)]

    perm = combinations(r1,p)
    ans = list(perm)
    return len(ans), ans

def getSubsets(k, n, arr):
    sieve()
    # Write your code here
    primeSum = 0
    for i in arr:
        if (i<=1): continue
        primeSum = primeSum + sum(primeList(i))
    
    primeSum = primeSum % 1000000
    
    ans, perm = countP(primeSum,k)

    return ans % 1000000007
    

getSubsets(3,3,[1,2,6])
