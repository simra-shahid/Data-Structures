# Q1. Given an Array return another array such that each element is the Product of the remaining elements in O(n)


def findSpecialProduct(inputArray):

    leftl = []
    leftl.append(inputArray[0])
    print(leftl)
    for i in range(1, len(inputArray)):
        leftl.append(inputArray[i]*leftl[i-1])
    
    left = [1] #Boundary Case Handling
    left.extend(leftl)

    print(left)
    
    rightl = [] 
    rightl.append(inputArray[-1])
    
    c = 1
    for i in range(len(inputArray)-2, -1, -1):
        rightl.append(inputArray[i]*rightl[c-1])
        c = c + 1
        
    right = rightl[::-1]
    right.append(1) #Boundary Case Handling
    print(right)
    
    result = []

    for i in range(1, len(inputArray)+1):
        result.append(left[i-1]*right[i])

    return result
    
    
    
