'''
Given an integer string and a target number, put any operators anywhere to get the target result
Example : 
input = 123 , target = 6
expression = 1*2*3, 1+2+3
input = 2314 , target = 29
expression = 2+31-4
'''

def find_exp(inp, target, cur, start):
    if start >= len(inp)-1:
        cur = cur + str(inp[start])
        if eval(cur) == target:
            print("Expression = ", cur, end = " ")
        cur = ""
        return 
    
    cur = cur + str(inp[start])

    
    for operator in ["+","-","*",""]:
        #print("Expression: ", cur +operator, "Start: ", start+1)
        find_exp(inp, target, cur + operator, start+1)

print("input = 123, target = 6", end=" ") 
find_exp('123', 6, '', 0)
print()

print("input = 125, target = 7", end=" ") 
find_exp('125', 7, '', 0)
print()

print("input = 2314, target = 29", end=" ") 
find_exp('2314', 29, '', 0)
print()

'''
Output:
input = 123, target = 6 Expression =  1+2+3 Expression =  1*2*3 
input = 125, target = 7 Expression =  1*2+5 Expression =  12-5 
input = 2314, target = 29 Expression =  2+31-4 
'''
