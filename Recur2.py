def calcSum(posInteger):  #function with one parameter
    if posInteger==0:      #ends execution when parameter reaches zero
        return 0
    else:
        return posInteger + calcSum(posInteger -2)#calculate sum of even integer
print(calcSum(10))
print(calcSum(6))
