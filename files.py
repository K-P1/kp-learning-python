"""#Reading a file as a text
file = open("demo text.txt")
#Still the same as
#file = open("demo text.txt","rt")
print(file.read())

file = open("datetime.py","rt")
print(file.read(10))
#eval(file.read())
"""
"""
my_file = open("demo text.txt")
print(my_file.readline())
print(my_file.readline())
print(my_file.readline())
print(my_file.readline())
print(my_file.readline())
#print(my_file.read())

#for line in my_file:
    #print(line)

"""



def  computFac(number):
    if number == 1:
        return 1
    else:
        return computFac(number - 1) * number

num = int(input("enter the number to be computed: "))
result = 1
while num != 0:
    result *= num
print(result)
#print(computFac(num))
"""
def  computFac(word):
    if number == 1:
        return 1
    else:
        return computFac(number - 1) * number

num = int(input("enter the number to be computed: "))
print(computFac(num))
"""
