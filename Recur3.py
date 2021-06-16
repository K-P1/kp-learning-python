def calcSum2(n):
    if n==1:
        return 1
    else:
        return calcSum2(n-1) + (1/n)
print(calcSum2(6))
