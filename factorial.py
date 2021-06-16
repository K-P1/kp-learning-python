number = input("Enter a number:\t")
while number.isdigit() is not True:
    number = input("Enter a number ejooor :\t")
else:
    fact = 1
    for n in range(1,int(number)+1):
        fact = fact * n
    print(fact)
