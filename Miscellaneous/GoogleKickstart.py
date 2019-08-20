# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000051061/0000000000161426
# Question : X or what?


def bits(n):
    return sum([int(i) for i in bin(n)[2:]])

def compute_ans(a=[10,21,3,7],
                changes=[[1,13],
                         [0,32],
                         [2,22]]
               ):

    ans = []
    odds = set()
    
    for i in range(0,len(a)):
        if bits(a[i])%2!=0:
            odds.add(i)
    
    for x in changes: 

        a[x[0]] = x[1]

        if bits(x[1])%2!=0:
            odds.add(x[0])
        else:
            odds.remove(x[0])
            
        if len(odds)%2==0:
            ans.append(len(a))
        else:
            o = list(sorted(odds))
            min1 = o[0]
            max1 = o[-1]
            ans.append(max(max1, (len(a)-(min1+1))))
        
    
    return ans
        

if __name__=="__main__":
    t = int(input())
    count=1
    while(t>0):
        n,q = input().split()
        a = list(map(int, input().split())) 
        changes =[]
        for i in range(0,int(q)):
            changes.append(list(map(int, input().split())) )
        ans = compute_ans(a,changes)

        print("Case #%(first)d:" % {"first": count}, *ans)
       
        count+=1
        print()
        t=t-1
