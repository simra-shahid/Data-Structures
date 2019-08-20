# FIND BIGGEST SUPER BALANCED BRACKET 
# example : (((()()()())))((()))
# SUPER BALANCED BRACKET  = (((()()()())))""((()))""
# BALANCED BRACKET = ()

# FIND BIGGEST SUPER BALANCED BRACKET 
def balancedBrackets(s):
    if len(s)<=1:
        return 0
    
    if len(s)==2:
        if s=="()":
            return 2
            
   
    stack =[]
    maximum = 0
    current = 0
    i=0
    
    while(i<len(s)):
        
        if len(stack)==0 and s[i]==")":
            i = i + 1
            continue

        elif s[i]=="(":
            stack.append("(")
            i+=1  
            
        else:    
            current=0
            while(i<len(s) and len(stack)!=0):
                if s[i]==")":
                    current+=2
                    stack.pop()
                    i+=1
                else:
                    #print(i," current ", current," stack removed ",stack)

                    #empty stack
                    stack=[]



            if(maximum<current):
                maximum=current

              
            
        #print(i-1, "-->", stack)    
    return maximum

list_of_inputs = ["((()))","()()","","(",")","()",")()()(())","(((()(()))()()))",")()("]

for i in list_of_inputs:
    print(i,"---->",balancedBrackets(i))
    
'''    
Output: 
  ((())) ----> 6
  ()() ----> 2
   ----> 0
  ( ----> 0
  ) ----> 0
  () ----> 2
  )()()(()) ----> 4
  (((()(()))()())) ----> 4
  )()( ----> 2
'''
