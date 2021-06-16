num = int(input("enter the number to be computed: "))
result = 1
while num != 1:
    result *= num
    print("num = ", num)
    print("result = ",result)
    num -= 1

print(result)
"""
def  computFac(number):
    if number == 1:
        return 1
    else:
        return computFac(number - 1) * number
"""
