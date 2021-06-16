"""
result = 0
x = 1

while x != 11: #base condition
    result += x
    x += 1
    
print(result)
"""
def recurssion(n):
    if n == 0:
        print("Value of n = ", n)
        return 0
    else:
        print("Value of n = ", n)
        return recurssion(n-1) + n

print(recurssion(10))
