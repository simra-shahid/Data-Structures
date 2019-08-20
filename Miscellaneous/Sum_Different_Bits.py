'''
Given an array Find sum of different corresponding bits for all pairs
Example: 
input = [1,3,5]
Binary Representation is: 
1 - 001
3 - 011
5 - 101

Pairs  = (1,1) + (1,3) + (1,5) + (3,3) + (3,1) + (3,5) + (5,1) + (5,3) + (5,5)
       =   0   +   1   +   1   +   0   +   1   +   2   +   1   +   2   +   0
Output = 8 
'''



def bit(n):
    return bin(n)[2:]

def method1(ar,n): #O(n^2)
    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            #print((ar[i],ar[j]), end=" ")
            s = int(bit(ar[i])) ^ int(bit(ar[j]))
            s = str(s)
            ans = ans + sum([int(k) for k in s])
            #print(" = ", sum([int(k) for k in s]))
      
      
        
    ans = ans*2
    return ans

def method2(ar,n):
    ans = 0
    for i in range(0,32): #O(n)
        
        count = 0
        for j in range(0,n):
            #check if ith bit of nth number is set
            if (ar[j]) & (1<<i):
                #set
                count = count+1
        
        ans = ans + (count * (n-count) * 2)
    
    
    return ans


if __name__=="__main__":
    t = int(input())
    while(t>0):
        n = int(input())
        a = list(map(int, input().split())) 
        print(method2(a,n))
        t=t-1
